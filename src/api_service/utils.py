import json
import os

from api_service.models import Car
from config.settings import BASE_DIR


def load_cars_from_json():
    file_path = os.path.join(BASE_DIR, 'cars_for_test.json')
    with open(file_path) as file:
        cars_data = json.load(file)

    cars = []
    for car_data in cars_data:
        car = Car(
            unique_number=car_data['unique_number'],
            current_location_id=car_data['current_location'],
            carrying_capacity=car_data['carrying_capacity']
        )
        cars.append(car)

    Car.objects.bulk_create(cars)
