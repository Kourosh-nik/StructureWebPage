from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *


app_name = 'user'

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('documents', DocumentView.as_view(), name='document'),
    path('add-document', AddDocumentView.as_view(), name='add-document'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('register', UserRegisterView.as_view(), name='register'),
]
