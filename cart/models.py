from django.db import models

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from products.models import Book

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='carts',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        verbose_name='Время создания корзины',
        auto_now_add=True)
    date_last_modified = models.DateTimeField(
        verbose_name='Время последнего изменения корзины',
        auto_now=True)

    def __str__(self):
        return "Корзина № {} для пользователя {}".format(self.pk, self.user)

    @property
    def products_count(self):
        products_sum = sum(
            product.quantity for product in self.products_in_cart.all())
        return products_sum

    @property
    def total_cost(self):
        total = sum(
            product.cost for product in self.products_in_cart.all())
        return total

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class ProductsInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='products_in_cart',
        on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book,
        related_name='books_in_cart',
        on_delete=models.CASCADE)
    quantity = models.IntegerField(
        verbose_name="",
        default=1)

    def __str__(self):
        return "Книга {} в корзине {}".format(self.book.name, self.cart.pk)

    def get_absolute_url(self):
        return reverse_lazy('cart:cart-list')

    @property
    def price(self):
        return self.book.price

    @property
    def cost(self):
        return self.book.price * self.quantity

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
        unique_together = (
            ('cart', 'book'),
        )
