from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'friender.settings')

app = Celery('friender')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'task_every_3m40s': {
        'task': 'friender.task_every_3min40sec',
        'schedule': 220,  
    },
    'task_three_times_hourly': {
        'task': 'friender.task_hourly_from_19_to_21',
        'schedule': crontab(hour='19-21', minute=0),
        'options': {'max_retries': 3},
    },
}