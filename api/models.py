from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    projects = models.ForeignKey("Project", on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("api:project", kwargs={
            "slug": self.slug
        })

    class Meta:
        ordering = ["-id"]