from django.urls import path, include

from .views import (
    RefSeriesListView,
    RefSeriesCreateView,
    RefSeriesUpdateView,
    RefSeriesDetailView,
    RefSeriesDeleteView
)

app_name = 'reference'

urlpatterns = [
    path('list/', RefSeriesListView.as_view(), name='series-list'),
    path('create/', RefSeriesCreateView.as_view(), name='series-create'),
    path('update/<int:pk>/', RefSeriesUpdateView.as_view(), name='series-update'),
    path('detail/<int:pk>/', RefSeriesDetailView.as_view(), name='series-detail'),
    path('delete/<int:pk>/', RefSeriesDeleteView.as_view(), name='series-delete')
]
