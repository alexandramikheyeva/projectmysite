from django.urls import path
from django.contrib.auth import views
from django.urls import path, include
from . import views


app_name = 'profile'

urlpatterns = [
    path('', views.profile,  name='profile'),
    path('update_profile/<int:pk>', views.AccountUpdate.as_view(), name="update-account"),

]