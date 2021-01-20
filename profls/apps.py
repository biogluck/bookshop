from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from .signals import profile_creator


class ProflsConfig(AppConfig):
    name = 'profls'

    def ready(self):
        # from django.contrib.auth import get_user_model
        # User = get_user_model()
        # print('ready')
        import profls.signals
        # post_save.connect(save_user_profile, sender=User)
