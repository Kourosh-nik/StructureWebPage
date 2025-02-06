from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView

# IndexView
class IndexView(ListView):
    template_name = "bim/index.html"
    context_object_name = "projects"
    model = BIMProject
    queryset = BIMProject.objects.all().order_by('-id')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = BimPanelModel.objects.first()
        context['categories'] = BIMCategory.objects.all()
        context['coworking'] = BIMCoworking.objects.all()
        context['trainings'] = BIMTraining.objects.all()
        return context


class CategoryView(ListView):
    template_name = "bim/category.html"
    context_object_name = "projects"
    model = BIMProject
    paginate_by = 18

    def get_queryset(self):
        category = BIMCategory.objects.filter(slug=self.kwargs['slug']).first()
        if category:
            self.extra_context = {
                'category': category
            }
            return BIMProject.objects.filter(category=category).order_by('-id')
        else:
            return BIMProject.objects.none()


class ProjectDetailView(DetailView):
    model = BIMProject
    template_name = 'bim/project-detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = BIMProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context

    def get_queryset(self):
        return BIMProject.objects.prefetch_related('images').all()
