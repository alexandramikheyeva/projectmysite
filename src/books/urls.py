from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
  #Autor
      path('autors/', views.AutorsView.as_view(), name="autors-view"),
      path('add_autors/', views.AddAutorsView.as_view(), name="add-autors"),
      path('delete_autors/<int:pk>', views.DeleteAutorsView.as_view(), name="delete-autors"),
      path('update_autors/<int:pk>', views.UpdateAutorsView.as_view(), name="update-autors"),
  #Genre
      path('genres/', views.GenreListView.as_view(), name="genre-list-view"),
      path('creategenre/', views.GenreCreateView.as_view(), name="create-genre"),
      path('deletegenre/<int:pk>', views.GenreDeleteView.as_view(), name="delete-genre"),
      path('updategenre/<int:pk>', views.GenreUpdateView.as_view(), name="update-genre"),
  #Publishing house
      path('publishing_house/', views.PublishingHouseView.as_view(), name="publishing-house-view"),
      path('create_publishing_house/', views.PublishingHouseCreateView.as_view(), name="create-publishing-house"),
      path('delete_publishing_house/<int:pk>', views.PublishingHouseDeleteView.as_view(), name="delete-publishing-house"),
      path('update_publishing_house/<int:pk>', views.PublishingHouseUpdateView.as_view(), name="update-publishing-house"),
  #Series
      path('series/', views.SeriesView.as_view(), name="series-view"),
      path('create_series/', views.SeriesCreateView.as_view(), name="create-series"),
      path('delete_series/<int:pk>', views.SeriesDeleteView.as_view(), name="delete-series"),
      path('update_series/<int:pk>', views.SeriesUpdateView.as_view(), name="update-series"),
  #Books
      path('books/', views.BookView.as_view(), name="book-view"),
      path('view_book/<int:pk>', views.ViewBook.as_view(), name="view-book"),
      path('create_books/', views.BookCreateView.as_view(), name="create-book"),
      path('delete_books/<int:pk>', views.BookDeleteView.as_view(), name="delete-book"),
      path('update_books/<int:pk>', views.BookUpdateView.as_view(), name="update-book"),

      path('success/', views.success_page, name="success-page")
]