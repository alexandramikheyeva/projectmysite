from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
# Create your models here.

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address_line_1 = models.CharField(max_length=100, null=True, blank=True)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email_profile = models.EmailField(null=True, blank=True)
    first_profile_name = models.CharField(max_length=100, null=True, blank=True)
    last_profile_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True, blank=True, default="Customers")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.user.username