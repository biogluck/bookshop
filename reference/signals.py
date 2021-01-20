from .models import Author
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Author)
def author_created(sender, instance, created, **kwargs):

    if created:
        print('author created')
