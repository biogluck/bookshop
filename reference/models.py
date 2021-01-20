from django.db import models

from django.urls import reverse_lazy, reverse
# Create your models here.


class Author(models.Model):
    name = models.CharField(
        verbose_name="Имя автора",  # Достоевский Фёдор Михайлович
        max_length=100)
    short_name = models.CharField(
        verbose_name="Сокращенное имя автора",  # Ф.М. Достоевский
        max_length=50,
        blank=True,
        null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reference:author-list')

    def get_view_url(self):
        return reverse('reference:author-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('reference:author-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('reference:author-delete', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('reference:author-create')
    """
    def get_add_url(self):
       reverse_lazy('ref-author:create', kwargs={'pk': self.pk }) 
       """


class Genre(models.Model):
    name = models.CharField(
        verbose_name="Жанр",
        max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('reference:genre-list')

    def get_view_url(self):
        return reverse('reference:genre-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('reference:genre-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('reference:genre-delete', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('reference:genre-create')


class Publisher(models.Model):
    name = models.CharField(
        verbose_name="Издательство",
        max_length=50)
    address = models.CharField(
        verbose_name="Адрес издательства",
        max_length=50)

    def __str__(self):
        return self.name + '; ' + self.address

    def get_absolute_url(self):
        return reverse('reference:publisher-list')

    def get_view_url(self):
        return reverse('reference:publisher-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('reference:publisher-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('reference:publisher-delete', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('reference:publisher-create')


class BookSeries(models.Model):
    name = models.CharField(
        verbose_name='Серия',
        max_length=50)
    publisher = models.ForeignKey(
        Publisher,
        related_name='series',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '. Изд-во ' + str(self.publisher.name)

    def get_absolute_url(self):
        return reverse('reference:series-list')

    def get_view_url(self):
        return reverse('reference:series-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('reference:series-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('reference:series-delete', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('reference:series-create')
