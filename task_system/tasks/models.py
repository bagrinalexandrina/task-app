from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from model_utils.fields import StatusField
from model_utils import Choices

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    STATUS = Choices('open', 'in progress', 'done')
    status = StatusField(choices_name='STATUS')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    task = ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text

