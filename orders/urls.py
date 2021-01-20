from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('order-checkout', views.OrderCheckoutView.as_view(), name="checkout"),
    path('order-success/<int:pk>/', views.OrderCheckoutSuccess.as_view(), name="success"),
    # path('list/', views.OrdersList.as_view(), name="list"),
    path('list-admin/', views.OrdersListAdmin.as_view(), name="list-admin"),
    path('order-view/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
