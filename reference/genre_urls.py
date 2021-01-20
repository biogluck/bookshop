from django.urls import path, include

from .views import (
RefGenreListView,
RefGenreCreateView,
RefGenreUpdateView,
RefGenreDetailView,
RefGenreDeleteView)

app_name = 'reference_genre'

urlpatterns = [
    path('list/', RefGenreListView.as_view(), name='genre-list'),
    path('create/', RefGenreCreateView.as_view(), name='genre-create'),
    path('update/<int:pk>/', RefGenreUpdateView.as_view(), name='genre-update'),
    path('detail/<int:pk>/', RefGenreDetailView.as_view(), name='genre-detail'),
    path('delete/<int:pk>/', RefGenreDeleteView.as_view(), name='genre-delete')
]