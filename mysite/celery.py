import os

from celery import Celery
from celery.schedules import crontab  # scheduler

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# HT 13. Celery beat
app.conf.beat_schedule = {
    # executes every odd hour
    'scraping-task-odd-hour': {
        'task': 'scraping.tasks.scraping_quotes',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # noqa: T001
