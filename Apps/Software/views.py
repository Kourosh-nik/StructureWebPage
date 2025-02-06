from .models import *
from django.db.models import Q

from django.views.generic import TemplateView, DetailView, ListView


class IndexView(ListView):
    template_name = "Software/index.html"
    context_object_name = 'projects'
    model = SoftProject
    queryset = SoftProject.objects.all().order_by('-id')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = SoftPanelModel.objects.first()
        context['categories'] = SoftCategory.objects.all()
        context['coworking'] = SoftCoworking.objects.all()
        context['trainings'] = SoftTraining.objects.all()
        return context

class CategoryView(ListView):
    template_name = "Software/category.html"
    context_object_name = "projects"
    model = SoftProject
    paginate_by = 18

    def get_queryset(self):
        category = SoftProject.objects.filter(slug=self.kwargs['slug']).first()
        if category:
            self.extra_context = {
                'category': category
            }
            return SoftProject.objects.filter(category=category).order_by('-id')
        else:
            return SoftProject.objects.none()


class ProjectDetailView(DetailView):
    model = SoftProject
    template_name = 'Software/project-detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = SoftProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context

    def get_queryset(self):
        return SoftProject.objects.prefetch_related('images').all()
