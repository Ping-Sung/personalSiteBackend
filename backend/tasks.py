from celery import shared_task
from datetime import datetime, timedelta
import os


@shared_task
def cleanup_expired_files():
    current_time = datetime.now()
    for filename in os.listdir('static/'):
        file_path = os.path.join('static/', filename)
        file_creation_time = datetime.fromtimestamp(
            os.path.getctime(file_path))
        if (current_time - file_creation_time) > timedelta(minutes=10):
            os.remove(file_path)
