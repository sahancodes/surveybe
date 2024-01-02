from celery import Celery
import os
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'surveybe.settings')

app = Celery('surveybe')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'print_text': {
    #     'task': 'notifications.tasks.print_text',
    #     'schedule': timedelta(seconds=10),  # Run every 5 minutes
    # },
    'todaysnotifications': {
        'task': 'notifications.tasks.todaysnotifications',
        'schedule': timedelta(seconds=10),
    }
}