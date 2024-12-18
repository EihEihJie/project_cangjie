from django.apps import AppConfig


class MyTestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_test_app'
    verbose_name = 'Django App'