from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView


class IndexView(ListView):
    template_name = "project_management/index.html"
    context_object_name = "projects"
    model = ProjManProject
    queryset = ProjManProject.objects.all().order_by("-id")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = ProjManPanelModel.objects.first()
        context['categories'] = ProjManCategory.objects.all()
        context['coworking'] = ProjManCoworking.objects.all()
        context['trainings'] = ProjManTraining.objects.all()
        return context


class CategoryView(ListView):
    template_name = "project_management/category.html"
    context_object_name = "projects"
    model = ProjManProject
    paginate_by = 18

    def get_queryset(self):
        category = ProjManProject.objects.filter(slug=self.kwargs['slug']).first()
        if category:
            self.extra_context = {
                'category': category
            }
            return ProjManProject.objects.filter(category=category).order_by('-id')
        else:
            return ProjManProject.objects.none()

class ProjectDetailView(DetailView):
    model = ProjManProject
    template_name = 'project_management/project-detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = ProjManProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context

    def get_queryset(self):
        return ProjManProject.objects.prefetch_related('images').all()

