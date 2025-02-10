from .models import *
from django.views.generic import DetailView, ListView
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse


class IndexView(View):
    def get(self, request):
        banner = STRPanelModel.objects.first()
        categories = STRCategory.objects.all().order_by('-id')
        coworking = STRCoworking.objects.all().order_by('-id')

        projects_list = STRProject.objects.all().order_by('-id')
        projects_paginator = Paginator(projects_list, 6)
        projects_page = request.GET.get('projects_page', 1)
        projects = projects_paginator.get_page(projects_page)

        trainings_list = STRTraining.objects.all().order_by('-id')
        trainings_paginator = Paginator(trainings_list, 4)
        trainings_page = request.GET.get('trainings_page', 1)
        trainings = trainings_paginator.get_page(trainings_page)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            projects_html = render(request, 'Structure_Design/projects-list.html', {'projects': projects}).content.decode(
                "utf-8")
            trainings_html = render(request, 'Structure_Design/training-list.html', {'trainings': trainings}).content.decode(
                "utf-8")
            return JsonResponse({'projects_html': projects_html, 'trainings_html': trainings_html})

        context = {
            'banner': banner,
            'categories': categories,
            'coworking': coworking,
            'projects': projects,
            'trainings': trainings,
        }

        return render(request, 'Structure_Design/index.html', context)


class CategoryView(ListView):
    template_name = "Structure_Design/category.html"
    context_object_name = "projects"
    model = STRProject
    paginate_by = 12

    def get_queryset(self):
        category = STRCategory.objects.filter(slug=self.kwargs['slug']).first()
        if category:
            self.extra_context = {
                'category': category
            }
            return STRProject.objects.filter(category=category).order_by('-id')
        else:
            return STRProject.objects.none()


class ProjectDetailView(DetailView):
    model = STRProject
    template_name = 'Structure_Design/project-detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return STRProject.objects.prefetch_related('images').all()


class CoworkingDetailView(DetailView):
    model = STRCoworking
    template_name = 'Structure_Design/coworking-detail.html'
    context_object_name = 'coworking'

    def get_queryset(self):
        return STRCoworking.objects.prefetch_related('images').all()
