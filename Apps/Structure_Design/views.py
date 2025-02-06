from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView


class IndexView(ListView):
    template_name = "Structure_Design/index.html"
    context_object_name = "projects"
    model = STRProject
    queryset = STRProject.objects.all().order_by('-id')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = STRPanelModel.objects.first()
        context['categories'] = STRCategory.objects.all()
        context['coworking'] = STRCoworking.objects.all()
        context['trainings'] = STRTraining.objects.all()
        return context


class CategoryView(ListView):
    template_name = "Structure_Design/category.html"
    context_object_name = "projects"
    model = STRProject
    paginate_by = 18

    def get_queryset(self):
        category = STRProject.objects.filter(slug=self.kwargs['slug']).first()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = STRProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context

    def get_queryset(self):
        return STRProject.objects.prefetch_related('images').all()
