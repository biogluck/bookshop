from django.contrib import admin
from django.urls import path, include

from userapp.views import (
    UserHomeView,
    AboutView,
    DeliveryView,
    UserBookList,
    UserBookDetailView,
)
from admincore.views import AdminView

# REST 
from rest_framework import routers
from products.apiviews import BookAPIList, AuthorAPIList, BookSetAPIList

# during development
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'books-set', BookSetAPIList)
router.register(r'author-set', AuthorAPIList)


urlpatterns = [
    path('admin-shop/ref/', include('reference.reference_urls')),
    path('admin-shop/products/', include('products.urls')),
    path('admin-shop/', include('admincore.urls')),
    path('cart/', include('cart.urls')),
    path('cart-s/', include('cart_sessions.urls')),
    path('orders/', include('orders.urls')),
    path('comments/', include('comments.urls')),
    path('search/', include('search.urls')),


    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', AboutView.as_view()),
    path('delivery/', DeliveryView.as_view()),
    path('book-list/', UserBookList.as_view()),
    path('book-detail/<int:pk>/', UserBookDetailView.as_view(), name='user-book-detail'),
    path('book-api-view/<int:pk>/', BookAPIList.as_view()),

    # path('author-api-view/', AuthorAPIList),

    path('', UserHomeView.as_view(), name='shop-home'),
    path('chat/', include('chat.urls')),  # chat

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ]
