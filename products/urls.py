from django.urls import path, include

from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDetailView,
    BookDeleteView,
    # BookStatsView
)

from .apiviews import BookAPIList

app_name = 'products'

urlpatterns = [ 
    path('book/list/', BookListView.as_view(), name='book-list'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('book/detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    # path('book/api/view/<int:pk>/', BookAPIList.as_view(), name='book-api-view'),
]