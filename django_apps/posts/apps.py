from django.apps import AppConfig

from test_task_drf.settings import DJANGO_APPS_FOLDER


APP_NAME = f'{DJANGO_APPS_FOLDER}.posts'


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = APP_NAME
