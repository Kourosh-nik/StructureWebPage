from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView


class IndexView(TemplateView):
    template_name = "Structure_Design/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = STRProject.objects.all()
        context['banner'] = STRPanelModel.objects.first()
        context['categories'] = STRCategory.objects.all()
        context['coworking'] = STRCoworking.objects.all()
        context['trainings'] = STRTraining.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = STRProject
    template_name = 'Structure_Design/detail.html'
    context_object_name = 'Project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = STRProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class CoworkingDetailView(DetailView):
    model = STRCoworking
    template_name = 'Structure_Design/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = STRCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = STRProject
    template_name = 'Structure_Design/store.html'
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
        context['categories'] = STRCategory.objects.all()
        context['gravity_systems'] = STRGravitySys.objects.all()
        context['lateral_systems'] = STRLateralSys.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context


class SearchView(ListView):
    model = STRProject
    template_name = 'Structure_Design/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return STRProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else STRProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = STRProject
    template_name = 'Structure_Design/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return STRProject.objects.filter(content__icontains='پروژه شاخص')


class CoworkingsView(ListView):
    model = STRCoworking
    template_name = 'Structure_Design/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in STRCoworking.objects.all():
            print(coworking.image.url)


        return STRCoworking.objects.filter(content__icontains='پروژه شاخص')


class MentoringView(TemplateView):
    template_name = 'Structure_Design/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = STRProject.objects.prefetch_related('images')
        context['Coworking'] = STRCoworking.objects.prefetch_related('images', 'category')
        return context

