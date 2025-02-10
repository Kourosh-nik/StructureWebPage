from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import *
from Apps.BIM.models import BIMCategory, BIMProject
from Apps.project_management.models import ProjManCategory, ProjManProject
from Apps.Retrofit.models import RetroCategory
from Apps.Software.models import SoftCategory
from Apps.Structure_Design.models import STRCategory, STRProject
from .forms import *
from django.contrib import messages
from Apps.Software.models import SoftProject


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
        panel = IndexDetailModel.objects.first()
        soft_projects = SoftProject.objects.all().order_by('-id')[:8]
        bim_projects = BIMProject.objects.all().order_by('-id')[:8]
        structure_categories = STRCategory.objects.all().order_by('-id')[:8]
        structure_projects = STRProject.objects.all().order_by('-id')[:6]

        context = {
            'panel': panel if panel else None,
            'soft_projects': soft_projects,
            'bim_projects': bim_projects,
            'structure_categories': structure_categories,
            'structure_projects': structure_projects,
        }
        return render(request, 'index.html', context)


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
