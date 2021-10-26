from django import forms
from .models import Project

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"