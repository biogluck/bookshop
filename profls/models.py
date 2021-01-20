from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Prf(models.Model):
    customer = models.OneToOneField(
        User,
        verbose_name="Покупатель",
        on_delete=models.CASCADE
        )
    delivery_address = models.TextField(
        "Адрес доставки",
        default='Необходимо заполнить'
    )

    def __str__(self):
        return self.delivery_address

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'
