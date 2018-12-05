from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class CSV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    file = models.FileField(default="static/Save/copyright.txt")

    def __str__(self):
        return f'{self.user.username} CSV'

    def get_absolute_url(self):
        return