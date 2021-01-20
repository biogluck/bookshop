from django.contrib import admin

# Register your models here.

from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_created',
        'date_last_modified']

    class Meta:
        model = models.Cart


class ProductsInCartAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'quantity',]

    class Meta:
        model = models.ProductsInCart


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.ProductsInCart, ProductsInCartAdmin)
