from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ForeignKey("Project", on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]

