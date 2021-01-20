from django.urls import path

from .views import (
    AdminView,
    AdminLoginView,
    AdminLogoutView,
    )

app_name = 'admincore'

urlpatterns = [
    path('', AdminView.as_view(), name='admin-main'),
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path('logout/', AdminLogoutView.as_view(), name='admin-logout'),
]
