from django.apps import AppConfig


class CallbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'callback'
    verbose_name = 'Обратный звонок'
    verbose_name_plural = 'Обратные звонки'
