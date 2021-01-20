from django.urls import path

from .views import SearchView, MakeSearchView

app_name = 'search'

urlpatterns = [
    path('', SearchView.as_view(), name='search-view'),
    path('results/', MakeSearchView.as_view(), name='search-results'),
]
