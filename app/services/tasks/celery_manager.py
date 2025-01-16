from celery import Celery
from app.config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["app.services.tasks.tasks"]
)

celery.conf.beat_schedule = {
    'check-notifications': {
        'task': 'process_notifications',
        'schedule': 30.0,
    },
}
