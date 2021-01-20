from django.urls import path, include

from .views import (
RefPublisherListView,
RefPublisherCreateView,
RefPublisherUpdateView,
RefPublisherDetailView,
RefPublisherDeleteView)

app_name = 'reference'

urlpatterns = [
    path('list/', RefPublisherListView.as_view(), name='publisher-list'),
    path('create/', RefPublisherCreateView.as_view(), name='publisher-create'),
    path('update/<int:pk>/', RefPublisherUpdateView.as_view(), name='publisher-update'),
    path('detail/<int:pk>/', RefPublisherDetailView.as_view(), name='publisher-detail'),
    path('delete/<int:pk>/', RefPublisherDeleteView.as_view(), name='publisher-delete')
]