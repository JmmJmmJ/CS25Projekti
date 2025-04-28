from django.db import models

from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
