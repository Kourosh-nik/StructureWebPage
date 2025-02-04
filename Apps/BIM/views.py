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


class CoworkingDetailView(DetailView):
    model = BIMCoworking
    template_name = 'bim/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = BIMCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = BIMProject
    template_name = 'bim/store.html'
    context_object_name = 'Project'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        selected_categories = self.request.GET.getlist('category')
        selected_floor_system = self.request.GET.get('floor_system')
        selected_lateral_system = self.request.GET.get('lateral_system')
        min_area = self.request.GET.get('min_area')
        max_area = self.request.GET.get('max_area')

        if selected_categories:
            query = query.filter(category__title__in=selected_categories)
        if min_area:
            query = query.filter(total_Area__gte=min_area)
        if max_area:
            query = query.filter(total_Area__lte=max_area)
        if selected_floor_system:
            query = query.filter(gravity_loading_sys__title=selected_floor_system)
        if selected_lateral_system:
            query = query.filter(lateral_loading_sys__title=selected_lateral_system)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BIMCategory.objects.all()
        context['gravity_systems'] = BIMGravitySys.objects.all()
        context['lateral_systems'] = BIMLateralSys.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context


class SearchView(ListView):
    model = BIMProject
    template_name = 'bim/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return BIMProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else BIMProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = BIMProject
    template_name = 'bim/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return BIMProject.objects.filter(content__icontains='پروژه شاخص')


class CoworkingsView(ListView):
    model = BIMCoworking
    template_name = 'bim/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in BIMCoworking.objects.all():
            print(coworking.image.url)

        return BIMCoworking.objects.filter(content__icontains='پروژه شاخص')


class MentoringView(TemplateView):
    template_name = 'bim/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = BIMProject.objects.prefetch_related('images')
        context['Coworking'] = BIMCoworking.objects.prefetch_related('images', 'category')
        return context