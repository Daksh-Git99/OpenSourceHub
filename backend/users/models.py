from django.db import models

# Create your models here.
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.username