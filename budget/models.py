from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Check to see if the default value can be outside of the value validator range


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    monthly_income = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    necessity_pct = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    savings_pct = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    fun_pct = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.user} Budget'

    def get_absolute_url(self):
        return reverse('save-progress')

    def get_success_url(self):
        return reverse('save-progress')