from django.urls import path
from directories import views

app_name = 'directories'
urlpatterns = [
    
    #Author
    path('view_authors', views.AuthorListView.as_view(), name='view_author.html'),
    path('add_author', views.AuthorCreateView.as_view(), name='add_author.html'),
    path('edit_author/<int:pk>', views.AuthorUpdateView.as_view(), name='edit_author.html'),
    path('delete_author/<int:pk>', views.AuthorDeleteView.as_view(), name='delete_author.html'),
    
    #Genres
    path('view_genres', views.GenresListView.as_view(), name='view_genres.html'),
    path('add_genre', views.GenresCreateView.as_view(), name='add_genre.html'),
    path('edit_genre/<int:pk>', views.GenresUpdateView.as_view(), name='edit_genre.html'),
    path('delete_genre/<int:pk>', views.GenresDeleteView.as_view(), name='delete_genre.html'),
    
    #Series
    path('view_series', views.SeriesListView.as_view(), name='view_series.html'),
    path('add_series', views.SeriesCreateView.as_view(), name='add_series.html'),
    path('edit_series/<int:pk>', views.SeriesUpdateView.as_view(), name='edit_series.html'),
    path('delete_series/<int:pk>', views.SeriesDeleteView.as_view(), name='delete_series.html'),
    
    #Publishing
    path('view_publishing', views.PublishingListView.as_view(), name='view_publishing.html'),
    path('add_publishing', views.PublishingCreateView.as_view(), name='add_publishing.html'),
    path('edit_publishing/<int:pk>', views.PublishingUpdateView.as_view(), name='edit_publishing.html'),
    path('delete_publishing/<int:pk>', views.PublishingDeleteView.as_view(), name='delete_publishing.html'),
    
    
  
]