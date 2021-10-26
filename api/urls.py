from django.contrib import admin
from django.urls import path, include
from .views import ProjectsListView, ProjectDetailView

urlpatterns = [
    path("", ProjectsListView.as_view(), name="projects"),
]
