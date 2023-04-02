from django.apps import AppConfig


class ConfigSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config_site'
    verbose_name = "Конфигурация"
    verbose_name_plural = "Конфигурации"
