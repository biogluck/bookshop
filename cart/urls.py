from django.urls import path

from .views import (
    CartListView,
    AddToCartView,
    CartItemDeleteView,
    ClearCartView,
)

app_name = "cart"

urlpatterns = [
    path('add/<int:product>/', AddToCartView.as_view(), name='add-to-cart'),
    path('list/', CartListView.as_view(), name='cart-list'),
    path('delete/<int:product>/', CartItemDeleteView.as_view(), name='cart-delete'),
    path('clear', ClearCartView.as_view(), name='cart-clear'),
]
