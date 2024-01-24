import logging
import os
import time
from datetime import datetime

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

@app.task()
def test_task():
    print('Celery task app begins')
    time.sleep(5)
    print('Celery task app slept for 5 seconds')
    print('All OK!')