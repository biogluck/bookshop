from django.urls import path

from .views import CartSessionListView, AddToCartSessionView, ClearCartSessionView

app_name = "cart_sess"

urlpatterns = [
    path('list/' , CartSessionListView.as_view(), name='cart-list'),
    path('add-s/<int:product>/' , AddToCartSessionView.as_view(), name='add-to-cart-session'),
    path('clear-s/' , ClearCartSessionView.as_view(), name='clear-cart-session'),
]