from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import *
from Apps.BIM.models import BIMCategory
from Apps.project_management.models import ProjManCategory
from Apps.Retrofit.models import RetroCategory
from Apps.Software.models import SoftCategory
from Apps.Structure_Design.models import STRCategory
from .forms import *
from django.contrib import messages


class HeaderView(View):
    def get(self, request):
        panel = SiteDetailModel.objects.first()

        # Categories of Menu Bar
        bim_categories = BIMCategory.objects.all()
        proj_categories = ProjManCategory.objects.all()
        retro_categories = RetroCategory.objects.all()
        str_categories = STRCategory.objects.all()
        soft_categories = SoftCategory.objects.all()

        context ={
            'panel': panel,
            'bim_categories': bim_categories,
            'proj_categories': proj_categories,
            'retro_categories': retro_categories,
            'str_categories': str_categories,
            'soft_categories': soft_categories,
        }
        return render(request, 'partial/header.html', context)

class FooterView(View):
    def get(self, request):
        panel = SiteDetailModel.objects.first()

        context = {
            'panel': panel
        }
        return render(request, 'partial/footer.html', context)

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutUsView(View):
    def get(self, request):
        panel = AboutUsDetailModel.objects.first()

        context = {
            'panel': panel
        }
        return render(request, 'home_Page/about-us.html', context)


class ContactUsView(View):
    def get(self, request):
        panel = SiteDetailModel.objects.first()

        context = {
            'panel': panel
        }
        return render(request, 'home_Page/contact-us.html', context)

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'فرم با موفقیت ارسال شد.')
        else:
            messages.add_message(request, messages.ERROR, 'خطا در ارسال فرم! لطفا با دقت فرم را تکمیل کنید')
        return redirect('home_Page:contact')
