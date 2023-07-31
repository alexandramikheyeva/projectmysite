from django.db import models
from django.shortcuts import render
from book.models import Book
from django.db.models import Q
# Create your views here.


def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__iexact=query) | 
            Q(authors__author_name__icontains=query)| 
            Q(series__series_name__icontains=query)| 
            Q(publication_year__iexact=query)|
            Q(binding__iexact=query)|
            Q(isbn__iexact=query)|
            Q(publisher__publishing_name__icontains=query))
    return render(request, 'search/search.html', {'results': results})