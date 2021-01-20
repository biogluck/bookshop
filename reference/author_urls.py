from django.urls import path, include

from .views import (
RefAuthorListView,
RefAuthorCreateView,
RefAuthorUpdateView,
RefAuthorDetailView,
RefAuthorDeleteView)

app_name = 'reference'

urlpatterns = [
    
    path('list/', RefAuthorListView.as_view(), name='author-list'),
    path('create/', RefAuthorCreateView.as_view(), name='author-create'),
    path('update/<int:pk>/', RefAuthorUpdateView.as_view(), name='author-update'),
    path('detail/<int:pk>/', RefAuthorDetailView.as_view(), name='author-detail'),
    path('delete/<int:pk>/', RefAuthorDeleteView.as_view(), name='author-delete')
]