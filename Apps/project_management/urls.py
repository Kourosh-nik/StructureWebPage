from django.urls import path
from . import views
from .views import IndexView

app_name = 'project_management'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),


    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('coworkings_detail/<int:id>/<slug:title>/', views.CoworkingDetailView.as_view(), name='coworking_detail'),
    path('store/', views.StoreView.as_view(), name='store'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('coworkings/', views.CoworkingsView.as_view(), name='coworkings'),
    path('mentoring/', views.MentoringView.as_view(), name='mentoring'),

]
