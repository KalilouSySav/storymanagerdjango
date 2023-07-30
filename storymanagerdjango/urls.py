"""
URL configuration for storymanagerdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/', views.get_project, name='get_project'),
    path('projects/all/', views.get_all_projects, name='get_all_projects'),
    path('projects/<int:project_id>/update/', views.update_project, name='update_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),

    path('projects/<int:project_id>/characters/', views.create_character, name='create_character'),
    path('projects/<int:project_id>/characters/<int:character_id>/', views.get_character, name='get_character'),
    path('projects/<int:project_id>/characters/all/', views.get_all_characters, name='get_all_characters'),
    path('projects/<int:project_id>/characters/<int:character_id>/update/', views.update_character, name='update_character'),
    path('projects/<int:project_id>/characters/<int:character_id>/delete/', views.delete_character, name='delete_character'),

    path('projects/<int:project_id>/scenarios/', views.create_scenario, name='create_scenario'),
    path('projects/<int:project_id>/scenarios/<int:scenario_id>/', views.get_scenario, name='get_scenario'),
    path('projects/<int:project_id>/scenarios/all/', views.get_all_scenarios, name='get_all_scenarios'),
    path('projects/<int:project_id>/scenarios/<int:scenario_id>/update/', views.update_scenario, name='update_scenario'),
    path('projects/<int:project_id>/scenarios/<int:scenario_id>/delete/', views.delete_scenario, name='delete_scenario'),

    path('projects/<int:project_id>/export/<str:format>/', views.export_project, name='export_project'),
    path('projects/import/', views.import_project, name='import_project'),
]
