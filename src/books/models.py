from django.db import models

# Create your models here.

class Book(models.Model):
    title  = models.CharField(max_length = 150)
    author = models.CharField(max_length = 30)
    description = models.CharField(max_length = 500, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)