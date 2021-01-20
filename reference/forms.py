from django import forms
from .models import Author, Genre, Publisher, BookSeries

class AuthorRefForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'short_name']

class GenreRefForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class PublisherRefForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']

class SeriesRefForm(forms.ModelForm):
    class Meta:
        model = BookSeries
        fields = ['name', 'publisher']

""" class AuthorRefUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'short_name'
        ]
 """
""" 
class AuthorRefCreateForm(forms.ModelForm):


    name = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'name'}))
    short_name = forms.CharField(widget=forms.widgets.Textarea())
 """