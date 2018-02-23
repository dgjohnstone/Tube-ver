from __future__ import unicode_literals
from ..login_app.models import User


from django.db import models

# Create your models here

class Video(models.Model):
    creator = models.ForeignKey(User, related_name = 'videos')
    video_number = models.IntegerField(blank=False, default=0, null=True)
    title = models.CharField(max_length=255)
    playlist = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    preperation = models.CharField(max_length=255)
    materials = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    