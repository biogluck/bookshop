from django.urls import path

from .views import UserHomeView

app_name = 'userapp'

urlpatterns = [
    path('shop-cart/', UserHomeView.as_view(), name='cart-sess'),
]
