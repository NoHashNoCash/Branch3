from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    transdate = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    type = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.user.username} Transaction'

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk':self.pk})