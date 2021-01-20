import re

from django.db import models
from django.utils.html import format_html


from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
# from django.core.validators import ValidationError

from reference.models import Author, Genre, Publisher, BookSeries
from django.urls import reverse


class Book(models.Model):
    BOOK_COVER_CHOICES = (
        ('ТВ', 'Твёрдый'),
        ('М', 'Мягкий'),
        ('ПЛ', 'Пластиковый'),
    )
    name = models.CharField(
        verbose_name="Название книги",
        max_length=200)
    cover = models.ImageField(
        verbose_name='Обложка',
        null=True,
        blank=True)
    price = models.DecimalField(
        verbose_name='Цена, BYN',
        max_digits=10,
        decimal_places=2)
    author = models.ManyToManyField(
        Author,
        verbose_name="Автор",
        related_name='books',)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    series = models.ForeignKey(
        BookSeries,
        verbose_name="Серия",
        on_delete=models.CASCADE,
        related_name='books',
        null=True,
        blank=True)
    genre = models.ManyToManyField(
        Genre,
        verbose_name="Жанр")
    year = models.PositiveSmallIntegerField(
        verbose_name="Год издания",
        blank=True,
        null=True)
    pages = models.PositiveSmallIntegerField(
        verbose_name="Количество страниц",
        blank=True, null=True)
    book_cover = models.CharField(
        verbose_name='Переплёт',
        max_length=10,
        choices=BOOK_COVER_CHOICES,
        default='ТВ')
    book_format = models.CharField(  # or choises?
        verbose_name='Формат книги',
        max_length=10,
        null=True,
        blank=True)
    isbn = models.SlugField(
        verbose_name='ISBN',
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex='^(97(8|9))?\d{9}[0-9xX]$',
            message='Input must be in 10- or 13-number ISBN format',
            code='invalid_isbn'),
        ]
    )
    weight = models.IntegerField(
        verbose_name='Вес книги, г',
        null=True,
        blank=True)
    age_restrictions = models.PositiveSmallIntegerField(
        verbose_name='Возрастные ограничения',
        blank=True,
        null=True)
    in_stock = models.IntegerField(
        verbose_name='Количество в наличии',
        blank=True, null=True)
    is_available = models.BooleanField(
        verbose_name='Доступность для заказа',
        default=True,
        blank=True, null=True)
    # or implement usnig choises 1, 2, ... 10
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[MaxValueValidator(
            limit_value=10), MinValueValidator(limit_value=1)],
        blank=True,
        null=True)
    date_created = models.DateField(
        verbose_name='Дата внесения в каталог',
        auto_now_add=True)
    date_last_modified = models.DateField(
        verbose_name='Дата последнего изменения карточки',
        auto_now=True)

    def get_absolute_url(self):
        return reverse('products:book-list')

    def get_view_url(self):
        return reverse('products:book-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('products:book-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('products:book-delete', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('products:book-create', kwargs={'pk': self.pk})

    @property
    def author_list(self):
        if self.author.all():
            return str(', '.join([str(a.name) for a in self.author.all()]))

    def genre_list(self):
        return ', '.join([str(a.name) for a in self.genre.all()])

    def __str__(self):
        full_name = self.name + ': ' + self.author_list
        if self.year:
            full_name += '. ' + str(self.year)
        return full_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
