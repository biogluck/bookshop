from django.contrib import admin
from orders import models


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "cart",
        "status",
        "created_time",
        "updated_time"
    )

    class Meta:
        model = models.Order

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderStatus)
