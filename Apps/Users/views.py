import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from .forms import *
import random
from utils.services import send_otp
from django.utils.timezone import now, timedelta
from Apps.Home_Page.models import SampleFileModel, SiteDetailModel
from django.db.models import Count
from ..BIM.models import BIMCategory
from ..Retrofit.models import RetroCategory
from ..Software.models import SoftCategory
from ..Structure_Design.models import STRCategory
from ..project_management.models import ProjManCategory


class HeaderView(LoginRequiredMixin, View):
    def get(self, request):
        panel = SiteDetailModel.objects.first()

        # Categories of Menu Bar
        bim_categories = BIMCategory.objects.all()
        proj_categories = ProjManCategory.objects.all()
        retro_categories = RetroCategory.objects.all()
        str_categories = STRCategory.objects.all()
        soft_categories = SoftCategory.objects.all()

        context = {
            'panel': panel,
            'bim_categories': bim_categories,
            'proj_categories': proj_categories,
            'retro_categories': retro_categories,
            'str_categories': str_categories,
            'soft_categories': soft_categories,
        }
        return render(request, 'Users/header.html', context)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Users/profile.html'

    def post(self, request):
        if 'fullname' in request.POST:
            form = UserProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'اطلاعات پروفایل با موفقیت بروزرسانی گردید')
            else:
                messages.add_message(request, messages.ERROR, 'خطا در بروزرسانی اطلاعات پروفایل')
        elif 'confirm_password' in request.POST:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                old_password = form.cleaned_data['old_password']
                user = request.user
                if user.check_password(old_password):
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()
                    logout(request)
                    return redirect('home_Page:index')
                else:
                    messages.add_message(request, messages.ERROR, 'رمز عبور اشتباه است')
            messages.add_message(request, messages.ERROR, 'خطا در بروزرسانی رمز عبور')
        return redirect('user:profile')



class DocumentView(LoginRequiredMixin, ListView):
    template_name = 'Users/documents.html'
    model = UserFileModel
    paginate_by = 20
    context_object_name = 'files'
    def get_queryset(self):
        files = UserFileModel.objects.filter(user=self.request.user)
        self.extra_context = files.aggregate(
            count=Count('id'),
            count_seen=Count('id', filter=models.Q(seen=True)),
            count_unseen=Count('id', filter=models.Q(seen=False))
        )
        return files.order_by('-id')



class AddDocumentView(LoginRequiredMixin, View):
    def get(self, request):
        files = SampleFileModel.objects.all().order_by('-id')
        context = {
            'files': files,
        }
        return render(request, 'Users/add-document.html', context)

    def post(self, request):
        form = UserFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            UserFileModel.objects.create(user=self.request.user, file=file)
            messages.add_message(request, messages.SUCCESS, 'فایل با موفقیت اپلود شد.')
        else:
            messages.add_message(request, messages.ERROR, 'خطا در آپلود فایل')
        return redirect('user:add-document')


class UserLoginView(View):
    def post(self, request):
        phone = request.POST.get('phone')  # دریافت داده از POST
        password = request.POST.get('password')

        user = authenticate(request, phone=phone, password=password)
        if user:
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": ""})
        else:
            return JsonResponse({"success": False, "message": "شماره یا رمز عبور اشتباه است"})


class UserRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd['phone']
            user = UserModel.objects.filter(phone=phone).first()
            if user:
                if user.ban:
                    return HttpResponse('کاربر ازسایت محروم شده است')
                return HttpResponse('کاربر وجود دارد')

            else:
                otp = OtpModel.objects.filter(phone=cd['phone']).first()
                if otp:
                    if otp.date + timedelta(minutes=2) < now():
                        code = random.randint(100000, 999999)
                        otp.code = code
                        otp.date = now()
                        send_otp(phone, code)
                        otp.save()
                else:
                    code = random.randint(100000, 999999)
                    OtpModel.objects.create(phone=phone, code=code)
                    send_otp(phone, code)
                return HttpResponse('ok')
        return render(request, 'user/form-errors.html', {'form': form})


class UserRegisterActivationView(View):
    def post(self, request):
        form = UserRegisterActivationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code = cd['code']
            phone = cd['phone']
            sending_code = OtpModel.objects.filter(phone=phone).first()
            if sending_code and sending_code.date + timedelta(minutes=10) > now():
                if str(sending_code.code) == str(code):
                    user = UserModel.objects.create_user(fullname=cd['fullname'], phone=phone,
                                                         password=cd['password'])
                    sending_code.delete()
                    login(request, user)
                    return HttpResponse('ok')
                else:
                    return HttpResponse('کد نادرست')
            return HttpResponse('نامعتبر')
        return render(request, 'user/form-errors.html', {'errors': form.errors})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home_Page:index')


class SendOtpCodeView(View):
    def post(self, request):
        form = SendOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd['phone']
            user = UserModel.objects.filter(phone=phone).first()
            if user:
                if user.ban:
                    messages.add_message(request, messages.ERROR, 'کاربر ازسایت محروم شده است')
                    return HttpResponse('کاربر ازسایت محروم شده است')
                else:
                    otp = OtpModel.objects.filter(phone=cd['phone']).first()
                    if otp:
                        if otp.date + timedelta(minutes=2) < now():
                            code = random.randint(100000, 999999)
                            otp.code = code
                            otp.date = now()
                            send_otp(phone, code)
                            otp.save()
                    else:
                        code = random.randint(100000, 999999)
                        OtpModel.objects.create(phone=phone, code=code)
                        send_otp(phone, code)
                    return HttpResponse('ok')

            else:
                return HttpResponse('کاربر وجود ندارد')

        return render(request, 'user/form-errors.html', {'form': form})


class PasswordForgetView(View):
    def get(self, request):
        return render(request, 'Users/forget-password.html')

    def post(self, request):
        form = ForgetForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd['phone']
            code = cd['code']
            user = UserModel.objects.filter(phone=phone).first()
            if user:
                if user.ban:
                    return HttpResponse('کاربر ازسایت محروم شده است')
                else:
                    sending_code = OtpModel.objects.filter(phone=phone).first()
                    if sending_code and sending_code.date + timedelta(minutes=10) > now():
                        if str(sending_code.code) == str(code):
                            sending_code.delete()
                            login(request, user)
                            return HttpResponse('ok')
                        else:
                            return HttpResponse('کد نادرست')
                    return HttpResponse('کد نادرست است')
            return HttpResponse('کاربر وجود ندارد')
        return HttpResponse('نامعتبر')
