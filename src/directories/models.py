from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your models here.

class Author(models.Model): 
    def __str__(self):
        return self.author_name
    
    def get_absolute_url(self):
        return '/success'
    
    author_name = models.CharField(
        verbose_name="Author name",  
        max_length=255
        )
    
    author_description = models.TextField(
        verbose_name="Author information",   
        null=True,
        blank=True 
           
    ) 

class Genres(models.Model): 
    def __str__(self):
        return self.genre_name
    
    def get_absolute_url(self):
        return '/success'
    
    
    genre_name = models.CharField(
        verbose_name="Genre name",  
        max_length=255
        )
    
    genre_description = models.TextField(
        verbose_name="Genre description",   
        null=True,
        blank=True        
    )

class Series(models.Model): 
    def __str__(self):
        return self.series_name
    
    def get_absolute_url(self):
        return '/success'
    
    series_name = models.CharField(
        verbose_name="Series count",  
        max_length=255
        )
    
    series_description = models.TextField(
        verbose_name="Series information",   
        null=True,
        blank=True        
    )    