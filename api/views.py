from rest_framework.serializers import Serializer
from .serializers import ProjectSerializer
from rest_framework.views import APIView
from .models import Project
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .forms import ProjectCreateForm

# Create your views here.

class ProjectsListView(LoginRequiredMixin, APIView):
    """
    List all projects, or create a new project.
    """

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(LoginRequiredMixin, APIView):
    """
    Retrieve, update or delete a project.
    """

    def get_object(self, project_id):
        try:
            return Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, project_id, format=None):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project_id, format=None):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, format=None):
        project = Project.objects.get(id=project_id)
        if not project.exists():
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        project = project.filter(user=request.user)
        if not project.exists():
            return Response({"message": "You cannot delete this Project"}, status=status.HTTP_404_NOT_FOUND)
        obj = project.first()
        obj.delete()
        return Response({"message": "Project deleted"}, status=status.HTTP_200_OK)

class ProjectCreateView(LoginRequiredMixin, APIView):
    """
    Create a new project.
    """

    def post(self, request):
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            completed = form.cleaned_data["completed"]
            duration = form.cleaned_data["duration"]
            date_created = form.cleaned_data["date_created"]
            project = Project(name=name, 
                            user=self.request.user,
                            description=description, 
                            completed=completed, 
                            duration=duration, 
                            date_created=date_created)
            project.save()
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"message": "Invalid form"}, status=status.HTTP_400_BAD_REQUEST)




