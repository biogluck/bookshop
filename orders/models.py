from django.db import models
from django.urls import reverse_lazy
from cart.models import Cart


class OrderStatus(models.Model):
    name = models.CharField(
        'Статус заказа',
        max_length=30)
    description = models.CharField(
        'Описание статуса',
        max_length=100,
        blank=True,
        null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name="Корзина",
        on_delete=models.PROTECT)
    status = models.ForeignKey(
        "orders.OrderStatus",
        verbose_name="Статус",
        on_delete=models.PROTECT)
    phone = models.CharField(
        verbose_name="Контактный телефон",
        max_length=16)
    email = models.EmailField(
        verbose_name="Электронная почта",
        null=True,
        blank=True,)
    delivery_address = models.TextField(
        verbose_name="Адрес доставки",
        null=True,
        blank=True,
    )
    comments = models.TextField(
        verbose_name="Дополнительная информация",
        null=True,
        blank=True,
    )
    created_time = models.DateTimeField(
        verbose_name="Время создания",
        auto_now=False,
        auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name="Время изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return "Заказ № {}, от {}".format(
            self.pk,
            self.created_time.strftime('%Y/%m/%d'))

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
