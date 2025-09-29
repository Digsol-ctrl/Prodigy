from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.Homepage.as_view(), name = "homepage" ),
    path("projects", views.Projectslist.as_view(), name="projects_list")
]