from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from directories import views
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

#Login
class CustomLoginView(LoginView):
    template_name = 'auntification/login.html'
    
    
#Logout
class CustomLogoutView(LogoutView):
    template_name = 'auntification/logout.html'
    
    
#Signup    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('staff:login')
    template_name = 'auntification/signup.html'