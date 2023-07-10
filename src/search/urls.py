from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from search.views import search


app_name = 'search'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
   
]
    