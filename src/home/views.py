from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from random import randint
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from pathlib import Path
from bookshop.models import Book

from . import models
from PIL import Image
#Homepage

class HomePage(generic.TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context.update({
            "object_list": books
        })
        return context

#Books
class BookView(generic.ListView):
    model = models.Book
    template_name = 'projectmysite/book/books.html'

class ViewBook(generic.ListView):
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'autor', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishing_house', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'book-shop/book/view_book.html'
    
class BookCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("staff:login")
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'autor', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishing_house', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'book-shop/book/create_books.html'

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("staff:login")
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'autor', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishing_house', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'book-shop/book/update_books.html'

    def get_success_url(self) -> str:
        resizer(self.object.book_image)
        return super().get_success_url()

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("staff:login")
    model = models.Book
    template_name = 'bookshop/book/delete_books.html'
    success_url = "/directories/success"

def resizer(image):
    extention = image.file.name.split('.')[-1]
    BASE_DIR = Path(image.file.name).resolve().parent
    file_name = Path(image.file.name).resolve().name.split('.')
    for m_basewidth in [250, 40]:
      im = Image.open(image.file.name)
      wpercent = (m_basewidth / float(im.size[0]))
      hsize = int(float(im.size[1]) * float(wpercent))
      im.thumbnail((m_basewidth, hsize), Image.Resampling.LANCZOS)
      im.save(str(BASE_DIR / "".join(file_name[:-1])) + f'_{m_basewidth}.' + extention)



def success_page(request):
    return render(
        request,
        template_name='projectmysite/success.html'
    )