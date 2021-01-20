from .models import Prf
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()


@receiver(post_save, sender=User)
def profile_creator(sender, instance, created, **kwargs):
    # print(sender, instance, kwargs)
    # created = kwargs.get('created')
    if created:
        print('created')
        # Prf.objects.create(
        #     customer=instance,
        #     delivery_address='empty'
        #     )

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwards):
#     if created:
#         print('hello')
        # email = EmailMessage('Subject', 'Body', to=['gmail.com'])
        # email.send()
