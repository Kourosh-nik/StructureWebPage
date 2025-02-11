from django.urls import path
from .views import *

app_name = 'home_Page'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact'),
    path('str-projects/<id>', STRProjectsView.as_view(), name='str_projects'),
]
