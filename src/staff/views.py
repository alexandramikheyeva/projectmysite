
from typing import Optional
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.views.generic import View
from django.http import HttpResponseRedirect

from bookshop.models import Book
# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = "staff/login.html"


class LogoutView(auth_views.LogoutView):
    next_page = 'homepage'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("staff:login")
    template_name = "staff/signup.html"