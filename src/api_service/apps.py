from django.apps import AppConfig


class ApiServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_service'

    def ready(self):
        from api_service.models import Location
        from api_service.tasks import load_location_data

        if not Location.objects.exists():
            load_location_data.delay()
