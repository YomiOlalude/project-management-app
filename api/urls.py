from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView

app_name = 'api'

urlpatterns = [
    path("", ProjectsListView.as_view(), name="projects"),
    path("project/<slug>", ProjectDetailView.as_view(), name="project"),
    path("create-project", ProjectCreateView.as_view(), name="create-project"),
]
