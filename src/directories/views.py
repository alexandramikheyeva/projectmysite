from django.shortcuts import render
from . import models
from django.views.generic.list import ListView
from django.views import generic
# Create your views here.

class AuthorListView(generic.ListView):
    model = models.Author
    template_name = "book_parametrs/author/view_authors.html"


class AuthorCreateView(generic.CreateView):
    model = models.Author
    fields = ['author_name', 'author_description']
    template_name = 'book_parametrs/author/add_author.html'
    
    
class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    success_url = '/success'
    fields = ['author_name', 'author_description']
    template_name = 'book_parametrs/author/edit_author.html'


class AuthorDeleteView(generic.DeleteView):
    model = models.Author
    success_url = '/success'
    template_name = 'book_parametrs/author/delete_author.html'
    

#Genres part
class GenresListView(generic.ListView):
    model = models.Genres
    template_name = "book_parametrs/genres/view_genres.html"


class GenresCreateView(generic.CreateView):
    model = models.Genres
    fields = ['genre_name', 'genre_description']
    template_name = 'book_parametrs/genres/add_genre.html'
    
    
class GenresUpdateView(generic.UpdateView):
    model = models.Genres
    success_url = '/success'
    fields = ['genre_name', 'genre_description']
    template_name = 'book_parametrs/genres/edit_genre.html'


class GenresDeleteView(generic.DeleteView):
    model = models.Genres
    success_url = '/success'
    template_name = 'book_parametrs/genres/delete_genre.html'
    

#Series
class SeriesListView(generic.ListView):
    model = models.Series
    template_name = "book_parametrs/series/view_series.html"


class SeriesCreateView(generic.CreateView):
    model = models.Series
    fields = ['series_name', 'series_description']
    template_name = 'book_parametrs/series/add_series.html'
    
    
class SeriesUpdateView(generic.UpdateView):
    model = models.Series
    success_url = '/success'
    fields = ['series_name', 'series_description']
    template_name = 'book_parametrs/series/edit_series.html'


class SeriesDeleteView(generic.DeleteView):
    model = models.Series
    success_url = '/success'
    template_name = 'book_parametrs/series/delete_series.html'
    

#Publishing
class PublishingListView(generic.ListView):
    model = models.Publishing
    template_name = "book_parametrs/publishing/view_publishing.html"


class PublishingCreateView(generic.CreateView):
    model = models.Publishing
    fields = ['publishing_name', 'publishing_description']
    template_name = 'book_parametrs/publishing/add_publishing.html'
    
    
class PublishingUpdateView(generic.UpdateView):
    model = models.Publishing
    success_url = '/success'
    fields = ['publishing_name', 'publishing_description']
    template_name = 'book_parametrs/publishing/edit_publishing.html'


class PublishingDeleteView(generic.DeleteView):
    model = models.Publishing
    success_url = '/success'
    template_name = 'book_parametrs/publishing/delete_publishing.html'