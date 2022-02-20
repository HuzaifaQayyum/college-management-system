from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
    icon_name = 'local_library'

    def ready(self):
        import library.signals.handlers