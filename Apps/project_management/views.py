from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView


class IndexView(TemplateView):
    template_name = "project_management/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = ProjManProject.objects.all()
        context['banner'] = ProjManPanelModel.objects.first()
        context['categories'] = ProjManCategory.objects.all()
        context['coworking'] = ProjManCoworking.objects.all()
        context['trainings'] = ProjManTraining.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = ProjManProject
    template_name = 'project_management/detail.html'
    context_object_name = 'Project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = ProjManProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context



class CoworkingDetailView(DetailView):
    model = ProjManCoworking
    template_name = 'project_management/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = ProjManCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = ProjManProject
    template_name = 'project_management/store.html'
    context_object_name = 'Project'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        selected_categories = self.request.GET.getlist('category')
        min_area = self.request.GET.get('min_area')
        max_area = self.request.GET.get('max_area')

        if selected_categories:
            query = query.filter(category__title__in=selected_categories)
        if min_area:
            query = query.filter(total_Area__gte=min_area)
        if max_area:
            query = query.filter(total_Area__lte=max_area)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjManCategory.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context


class SearchView(ListView):
    model = ProjManProject
    template_name = 'project_management/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return ProjManProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else ProjManProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = ProjManProject
    template_name = 'project_management/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return ProjManProject.objects.filter(content__icontains='پروژه شاخص')



class CoworkingsView(ListView):
    model = ProjManCoworking
    template_name = 'project_management/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in ProjManCoworking.objects.all():
            print(coworking.image.url)


        return ProjManCoworking.objects.filter(content__icontains='پروژه شاخص')



class MentoringView(TemplateView):
    template_name = 'project_management/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = ProjManProject.objects.prefetch_related('images')
        context['Coworking'] = ProjManCoworking.objects.prefetch_related('images', 'category')
        return context

