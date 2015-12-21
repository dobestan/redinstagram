from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.environ['DJANGO_SETTINGS_MODULE'],
)

app = Celery("redinstagram")

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)