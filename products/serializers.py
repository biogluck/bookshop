from rest_framework import serializers

from .models import Book
from reference.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'pk',
            'name',
            'short_name',
        )


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=True)
    #  author = serializers.StringRelatedField(many=False)

    genre = serializers.StringRelatedField(many=True)
    publisher = serializers.StringRelatedField(many=False)
    series = serializers.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = (
            'name',
            'cover',
            'author',
            'genre',
            'publisher',
            'series',
            'year',
            'price',
        )
