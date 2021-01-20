from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    comment = models.TextField(
        verbose_name="Коментарий"
    )
    commentator = models.ForeignKey(
        User,
        related_name='comments',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    date_created = models.DateTimeField(
        verbose_name='Время создания комментария',
        auto_now_add=True)
    date_last_modified = models.DateTimeField(
        verbose_name='Время последнего изменения комментария',
        auto_now=True)

    def __str__(self):
        return self.comment
