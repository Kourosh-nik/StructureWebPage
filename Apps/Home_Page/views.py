from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib import messages
from django.contrib.postgres.search import TrigramSimilarity
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import *
from .models import *
from Apps.Retrofit.models import RetroCategory, RetroProject, RetroCoworking, RetroTraining
from Apps.Software.models import SoftCategory, SoftProject, SoftTraining
from Apps.Structure_Design.models import STRCategory, STRProject, STRCoworking, STRTraining
from Apps.BIM.models import BIMCategory, BIMProject, BIMCoworking, BIMTraining
from Apps.project_management.models import ProjManCategory, ProjManProject, ProjManCoworking, ProjManTraining



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
        retrofit_projects = RetroProject.objects.all().order_by('-id')[:8]

        context = {
            'panel': panel if panel else None,
            'soft_projects': soft_projects,
            'bim_projects': bim_projects,
            'structure_categories': structure_categories,
            'structure_projects': structure_projects,
            'retrofit_projects': retrofit_projects,
        }
        return render(request, 'index.html', context)


class SearchView(View):
    def get(self, request):
        query = request.GET.get('search', '')
        page_number = request.GET.get('page', 1)

        if query:
            # Helper function to search models
            def search_models(models, category=True):
                querysets = []
                for model in models:
                    if category:
                        queryset = model.objects.annotate(
                            similarity=TrigramSimilarity('title', query) + TrigramSimilarity('category__title', query)
                        ).filter(similarity__gt=0.1).values('id', 'title', 'category__title', 'similarity', 'image')
                    else:
                        queryset = model.objects.annotate(
                            similarity=TrigramSimilarity('title', query)
                        ).filter(similarity__gt=0.1).values('id', 'title', 'similarity', 'image')
                    querysets.append(queryset)
                return querysets

            # Define models for each category
            project_models = [ProjManProject, STRProject, BIMProject, RetroProject, SoftProject]
            coworking_models = [STRCoworking, ProjManCoworking, RetroCoworking, BIMCoworking]
            training_models = [BIMTraining, SoftTraining, RetroTraining, STRTraining, ProjManTraining]

            # Get results for each category
            project_results = search_models(project_models, category=True)
            coworking_results = search_models(coworking_models, category=True)
            training_results = search_models(training_models, category=False)

            # Combine results and order by ID
            from itertools import chain

            def combine_and_paginate(querysets):
                combined = list(chain(*querysets))  # Combine querysets more efficiently
                return combined

            all_project_results = combine_and_paginate(project_results)
            all_coworking_results = combine_and_paginate(coworking_results)
            all_training_results = combine_and_paginate(training_results)

            # Paginate results
            projects_paginator = Paginator(all_project_results, 1)
            projects_page = request.GET.get('projects_page', 1)
            projects = projects_paginator.get_page(projects_page)

            coworking_paginator = Paginator(all_coworking_results, 1)
            coworking_page = request.GET.get('coworking_page', 1)
            coworking = coworking_paginator.get_page(coworking_page)

            trainings_paginator = Paginator(all_training_results, 1)
            trainings_page = request.GET.get('trainings_page', 1)
            trainings = trainings_paginator.get_page(trainings_page)

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Send data for AJAX requests
                projects_html = render(request, 'home_Page/projects-list.html', {'projects': projects}).content.decode("utf-8")
                coworking_html = render(request, 'home_Page/coworking-list.html', {'coworking': coworking}).content.decode("utf-8")
                trainings_html = render(request, 'home_Page/training-list.html', {'trainings': trainings}).content.decode("utf-8")

                # Send HTML with pagination data
                return JsonResponse({
                    'projects_html': projects_html,
                    'coworking_html': coworking_html,
                    'trainings_html': trainings_html,
                    'projects_page_range': list(projects.paginator.page_range),
                    'coworking_page_range': list(coworking.paginator.page_range),
                    'trainings_page_range': list(trainings.paginator.page_range),
                    'projects_has_previous': projects.has_previous(),
                    'projects_has_next': projects.has_next(),
                    'coworking_has_previous': coworking.has_previous(),
                    'coworking_has_next': coworking.has_next(),
                    'trainings_has_previous': trainings.has_previous(),
                    'trainings_has_next': trainings.has_next(),
                    'projects_current_page': projects.number,
                    'coworking_current_page': coworking.number,
                    'trainings_current_page': trainings.number
                })
            else:
                # Return full page with rendered HTML
                return render(request, 'home_Page/search.html', {
                    'query': query,
                    'projects': projects,
                    'coworking': coworking,
                    'training': trainings
                })
        else:
            return render(request, 'home_Page/search.html', {
                'query': '',
                'projects': [],
                'coworking': [],
                'training': []
            })


class STRProjectsView(ListView):
    template_name = 'home_Page/structure_design.html'
    model = STRProject
    context_object_name = 'projects'

    def get_queryset(self):
        id = self.kwargs.get('id', '0')
        if id == '0':
            return STRProject.objects.all().order_by('-id')[:6]
        return STRProject.objects.filter(category_id=id).order_by('-id')[:6]


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
