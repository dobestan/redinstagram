from django.db.models.signals import post_save
from django.dispatch import receiver

from redinstagram.models import Post


@receiver(post_save, sender=Post)
def create_hash_id(sender, instance, created, **kwargs):
    if created:
        instance._create_hash_id()
