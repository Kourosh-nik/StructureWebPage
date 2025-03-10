from django.urls import path
from .views import *

app_name = 'bim'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('project/<slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('coworking/<slug>/', CoworkingDetailView.as_view(), name='coworking_detail'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),

]
