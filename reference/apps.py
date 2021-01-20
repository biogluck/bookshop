from django.apps import AppConfig


class ReferenceConfig(AppConfig):
    name = 'reference'

    def ready(self):
        from .signals import author_created
