from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic

# Create your views here.

class BookListView(generic.ListView):
    model = models.Book
    template_name = "book/book_view_all.html"


class BookCreateView(generic.CreateView):
    model = models.Book
    template_name = 'book/book_add.html'
    success_url = reverse_lazy('book:book_view_all.html')
    fields = ['title', 'cover_image', 'price', 'authors',
              'series','genres', 'publication_year', 'pages', 'binding',
              'format', 'isbn', 'weight', 'age_limit',
              'publisher', 'quantity_available', 'is_active', 'rating']


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'book/book_detail.html'


class BookUpdateView(generic.UpdateView):
    model = models.Book
    template_name = 'book/book_update.html'
    fields = ['title', 'cover_image', 'price', 'authors',
              'series','genres', 'publication_year', 'pages', 'binding',
              'format', 'isbn', 'weight', 'age_limit',
              'publisher', 'quantity_available', 'is_active', 'rating']


class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('/success')