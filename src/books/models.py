from django.db import models

# Create your models here.

class Book(models.Model):
    title  = models.CharField(max_length = 150)
    author = models.CharField(max_length = 30)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)