from django.urls import path
from .views import *

app_name = 'project_management'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
path('project/<slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),

]
