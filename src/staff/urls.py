from django.urls import path
from django.contrib.auth import views
from django.urls import path, include
from . import views


app_name = 'staff'
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("logout/", views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]