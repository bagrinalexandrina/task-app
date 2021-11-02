from django.db import models
from django.conf import settings
from users.models import User


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()


    def __str__(self):
        return self.title