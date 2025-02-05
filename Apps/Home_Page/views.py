from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *
from Apps.BIM.models import BIMCategory
from Apps.project_management.models import ProjManCategory
from Apps.Retrofit.models import RetroCategory
from Apps.Software.models import SoftCategory
from Apps.Structure_Design.models import STRCategory


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
        return render(request, 'home_Page/about-us.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'home_Page/contact.html')