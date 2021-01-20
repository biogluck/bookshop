from django.forms import Form, IntegerField, BooleanField
from django.forms import ModelForm, HiddenInput


class AddToCartSessionForm(Form):
    quantity = IntegerField()
    update = BooleanField(required=False, initial=False, widget=HiddenInput)

