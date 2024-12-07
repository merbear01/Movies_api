from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieapi.settings')

app = Celery('movieapi')

# Using a string here means the worker doesn’t have to serialize the config object.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks from all installed apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
