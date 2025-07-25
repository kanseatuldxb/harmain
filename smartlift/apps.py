from django.apps import AppConfig


class SmartliftConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartlift'

    def ready(self):
        import smartlift.signals  # Make sure to import the signal handler
