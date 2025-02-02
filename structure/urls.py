from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.Home_Page.urls', namespace='home_Page')),

    path('bim/', include('Apps.BIM.urls', namespace='bim')),
    path('project_management/', include('Apps.project_management.urls', namespace='project_management')),
    path('structure_design/', include('Apps.Structure_Design.urls', namespace='Structure_Design')),
    path('retrofit/', include('Apps.Retrofit.urls', namespace='Retrofit')),
    path('software/', include('Apps.Software.urls', namespace='Software')),
    path('user/', include('Apps.Users.urls', namespace='user')),


]