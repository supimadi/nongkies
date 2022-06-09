from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from . models import Reviewer

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Reviewer.objects.create(account=instance, bio="")
  
#  @receiver(post_save, sender=User)
#  def save_profile(sender, instance, **kwargs):
#          instance.reviewer.save()
