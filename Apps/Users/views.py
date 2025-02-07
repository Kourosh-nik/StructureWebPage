import json
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from .forms import *
import random
from utils.services import send_otp
from django.utils.timezone import now, timedelta
from Apps.Home_Page.models import SampleFileModel
from django.db.models import Count


class HeaderView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'Users/header.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Users/profile.html'


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
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd['phone']
            user = UserModel.objects.filter(phone=phone).first()
            if user:
                time.sleep(2)
                check_password = user.check_password(cd['password'])
                if check_password:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.add_message(request, messages.ERROR, 'شماره یا رمز عبور اشتباه است')
                    return redirect(request.META['HTTP_REFERER'])
            else:
                messages.add_message(request, messages.ERROR, 'شماره یا رمز عبور اشتباه است')
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect(request.META['HTTP_REFERER'])


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
        return redirect('home_page:index')


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
        return render(request, 'user/forget.html')

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
