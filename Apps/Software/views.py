from .models import *
from django.db.models import Q

from django.views.generic import TemplateView, DetailView, ListView


class IndexView(TemplateView):
    template_name = "Software/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = SoftProject.objects.all()
        context['banner'] = SoftPanelModel.objects.first()
        context['categories'] = SoftCategory.objects.all()
        context['coworking'] = SoftCoworking.objects.all()
        context['trainings'] = SoftTraining.objects.all()
        return context

class ProjectDetailView(DetailView):
    model = SoftProject
    template_name = 'Software/detail.html'
    context_object_name = 'Project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = SoftProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class CoworkingDetailView(DetailView):
    model = SoftCoworking
    template_name = 'Software/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = SoftCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = SoftProject
    template_name = 'Software/store.html'
    context_object_name = 'Project'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        selected_categories = self.request.GET.getlist('category')
        selected_soft_version = self.request.GET.get('soft_version')
        selected_soft_fee = self.request.GET.get('soft_fee')
        min_area = self.request.GET.get('min_area')
        max_area = self.request.GET.get('max_area')

        if selected_categories:
            query = query.filter(category__title__in=selected_categories)
        if min_area:
            query = query.filter(total_Area__gte=float(min_area))
        if max_area:
            query = query.filter(total_Area__lte=float(max_area))
        if selected_soft_version:
            query = query.filter(gravity_loading_sys__title=selected_soft_version)
        if selected_soft_fee:
            query = query.filter(lateral_loading_sys__title=selected_soft_fee)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = SoftCategory.objects.all()
        context['soft_versions'] = SoftVersion.objects.all()
        context['soft_fees'] = SoftFee.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context



class SearchView(ListView):
    model = SoftProject
    template_name = 'Software/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return SoftProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else SoftProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = SoftProject
    template_name = 'Software/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return SoftProject.objects.filter(content__icontains='پروژه شاخص')


class CoworkingsView(ListView):
    model = SoftCoworking
    template_name = 'Software/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in SoftCoworking.objects.all():
            print(coworking.image.url)


        return SoftCoworking.objects.filter(content__icontains='پروژه شاخص')


class MentoringView(TemplateView):
    template_name = 'Software/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = SoftProject.objects.prefetch_related('images')
        context['Coworking'] = SoftCoworking.objects.prefetch_related('images', 'category')
        return context
