from django import forms
from .models import Book
from django.core.validators import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
        'name',
        'cover',
        'price',
        'author',
        'series',
        'genre',
        'year',
        'pages',
        'book_cover',
        'book_format',
        'isbn',
        'weight',
        'age_restrictions',
        'publisher',
        'in_stock',
        'is_available',
        'rating',]

""" 
    def clean(self): # clean all form
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price != 5:
            raise ValidationError('Error message!') #  from django.core.validators import ValidationError
        return cleaned_data

    def clean_price(self): # clean field 
        price = self.cleaned_data.get('price')
        self.add_error('price', 'message')
        if price != 5:
            raise ValidationError('Error message!') #  from django.core.validators import ValidationError

 """            