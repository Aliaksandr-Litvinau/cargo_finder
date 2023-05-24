import csv
import os

from celery import shared_task

from api_service.models import Location
from config.settings import BASE_DIR


@shared_task
def load_location_data():
    file_path = os.path.join(BASE_DIR, 'uszips.csv')
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            zip_code = row['zip']
            if not Location.objects.filter(zip_code=zip_code).exists():
                location = Location(
                    city=row['city'],
                    state=row['state_id'],
                    zip_code=zip_code,
                    latitude=row['lat'],
                    longitude=row['lng'],
                )
                location.save()
