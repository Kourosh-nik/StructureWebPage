from django.urls import path
from .views import *


app_name = 'user'

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('document', DocumentView.as_view(), name='document'),
]
