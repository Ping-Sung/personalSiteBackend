from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置默认Django设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# 使用以`CELERY`开头的配置来设置Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动加载任务
app.autodiscover_tasks(['backend.tasks'])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
