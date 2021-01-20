from django.forms import ModelForm, HiddenInput
from django.forms import Form, IntegerField, BooleanField
from .models import Cart, ProductsInCart


class AddToCartForm(ModelForm):

    class Meta:
        model = ProductsInCart
        fields = [
            'book',
            'quantity']
        widgets = {
            'book': HiddenInput(),
        }


class AddToCartSessionForm(Form):
    quantity = IntegerField()
    update = BooleanField(required=False, initial=False, widget=HiddenInput)
