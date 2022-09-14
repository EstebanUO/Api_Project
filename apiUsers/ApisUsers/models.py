from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, default='')
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=70, blank=False, default='')