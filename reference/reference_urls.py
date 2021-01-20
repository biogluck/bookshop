from django.urls import path, include

from .views import (
    # Author 
    RefAuthorListView,
    RefAuthorCreateView,
    RefAuthorUpdateView,
    RefAuthorDetailView,
    RefAuthorDeleteView,
    # Genre
    RefGenreListView,
    RefGenreCreateView,
    RefGenreUpdateView,
    RefGenreDetailView,
    RefGenreDeleteView,
    # Publisher
    RefPublisherListView,
    RefPublisherCreateView,
    RefPublisherUpdateView,
    RefPublisherDetailView,
    RefPublisherDeleteView,
    # Series
    RefSeriesListView,
    RefSeriesCreateView,
    RefSeriesUpdateView,
    RefSeriesDetailView,
    RefSeriesDeleteView,
)

app_name = 'reference'

urlpatterns = [
    # Author
    path('author/list/', RefAuthorListView.as_view(), name='author-list'),
    path('author/create/', RefAuthorCreateView.as_view(), name='author-create'),
    path('author/update/<int:pk>/', RefAuthorUpdateView.as_view(), name='author-update'),
    path('author/detail/<int:pk>/', RefAuthorDetailView.as_view(), name='author-detail'),
    path('author/delete/<int:pk>/', RefAuthorDeleteView.as_view(), name='author-delete'),
    # Genre
    path('genre/list/', RefGenreListView.as_view(), name='genre-list'),
    path('genre/create/', RefGenreCreateView.as_view(), name='genre-create'),
    path('genre/update/<int:pk>/', RefGenreUpdateView.as_view(), name='genre-update'),
    path('genre/detail/<int:pk>/', RefGenreDetailView.as_view(), name='genre-detail'),
    path('genre/delete/<int:pk>/', RefGenreDeleteView.as_view(), name='genre-delete'),
    # Publisher
    path('publisher/list/', RefPublisherListView.as_view(), name='publisher-list'),
    path('publisher/create/', RefPublisherCreateView.as_view(), name='publisher-create'),
    path('publisher/update/<int:pk>/', RefPublisherUpdateView.as_view(), name='publisher-update'),
    path('publisher/detail/<int:pk>/', RefPublisherDetailView.as_view(), name='publisher-detail'),
    path('publisher/delete/<int:pk>/', RefPublisherDeleteView.as_view(), name='publisher-delete'),
    # Series
    path('series/list/', RefSeriesListView.as_view(), name='series-list'),
    path('series/create/', RefSeriesCreateView.as_view(), name='series-create'),
    path('series/update/<int:pk>/', RefSeriesUpdateView.as_view(), name='series-update'),
    path('series/detail/<int:pk>/', RefSeriesDetailView.as_view(), name='series-detail'),
    path('series/delete/<int:pk>/', RefSeriesDeleteView.as_view(), name='series-delete'),
]