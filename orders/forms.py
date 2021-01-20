from django import forms
from .models import Order


class CheckoutOrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [
            'cart',
            'status',
            'phone',
            'email',
            'delivery_address',
            'comments',
        ]
        widgets = {
            'cart': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }