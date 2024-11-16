from django.urls import path
from . import views

app_name = 'homePage'

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('<int:id>/<str:title>/', views.detail, name='detail'),
]