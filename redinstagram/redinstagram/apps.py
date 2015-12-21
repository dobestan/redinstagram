from django.apps import AppConfig


class RedinstagramAppConfig(AppConfig):
    name = 'redinstagram'

    def ready(self):
        from redinstagram.signals.post_save import create_hash_id
