from django.apps import AppConfig


class ApiServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_service'

    def ready(self):
        from api_service.models import Location, Car
        from api_service.tasks import load_location_data
        from api_service.utils import load_cars_from_json

        if not Location.objects.exists():
            load_location_data.delay()

        if not Car.objects.exists():
            load_cars_from_json()
