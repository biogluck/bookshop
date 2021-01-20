from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Publisher, BookSeries

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(BookSeries)
