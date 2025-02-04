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


class ProjectDetailView(DetailView):
    model = RetroProject
    template_name = 'Retrofit/detail.html'
    context_object_name = 'Project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = RetroProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class CoworkingDetailView(DetailView):
    model = RetroCoworking
    template_name = 'Retrofit/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = RetroCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = RetroProject
    template_name = 'Retrofit/store.html'
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
        context['categories'] = RetroCategory.objects.all()
        context['gravity_systems'] = RetroGravitySys.objects.all()
        context['lateral_systems'] = RetroLateralSys.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context





class SearchView(ListView):
    model = RetroProject
    template_name = 'Retrofit/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return RetroProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else RetroProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = RetroProject
    template_name = 'Retrofit/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return RetroProject.objects.filter(content__icontains='پروژه شاخص')



class CoworkingsView(ListView):
    model = RetroCoworking
    template_name = 'Retrofit/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in RetroCoworking.objects.all():
            print(coworking.image.url)


        return RetroCoworking.objects.filter(content__icontains='پروژه شاخص')


class MentoringView(TemplateView):
    template_name = 'Retrofit/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = RetroProject.objects.prefetch_related('images')
        context['Coworking'] = RetroCoworking.objects.prefetch_related('images', 'category')
        return context
