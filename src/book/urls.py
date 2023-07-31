from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('view_book', views.BookListView.as_view(), name='book_view_all.html'),
    path('book_add', views.BookCreateView.as_view(), name='book_add.html'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail.html'),
    path('book_update/<int:pk>', views.BookUpdateView.as_view(), name='book_update.html'),
    path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete.html')
    ]