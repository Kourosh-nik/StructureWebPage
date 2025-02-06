from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView


class IndexView(ListView):
    template_name = "Retrofit/index.html"
    context_object_name = "projects"
    model = RetroProject
    queryset = RetroProject.objects.all().order_by('-id')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = RetroPanelModel.objects.first()
        context['categories'] = RetroCategory.objects.all()
        context['coworking'] = RetroCoworking.objects.all()
        context['trainings'] = RetroTraining.objects.all()
        return context


class CategoryView(ListView):
    template_name = "Retrofit/category.html"
    context_object_name = "projects"
    model = RetroProject
    paginate_by = 18

    def get_queryset(self):
        category = RetroProject.objects.filter(slug=self.kwargs['slug']).first()
        if category:
            self.extra_context = {
                'category': category
            }
            return RetroProject.objects.filter(category=category).order_by('-id')
        else:
            return RetroProject.objects.none()


class ProjectDetailView(DetailView):
    model = RetroProject
    template_name = 'Retrofit/project-detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = RetroProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context

    def get_queryset(self):
        return RetroProject.objects.prefetch_related('images').all()