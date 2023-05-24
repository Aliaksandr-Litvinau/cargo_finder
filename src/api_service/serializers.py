from geopy.distance import distance
from rest_framework import serializers

from api_service.models import Cargo, Location


class CargoSerializer(serializers.ModelSerializer):
    zip_code_pick_up = serializers.CharField(max_length=10, write_only=True)
    zip_code_delivery = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = Cargo
        fields = ['zip_code_pick_up', 'zip_code_delivery', 'weight', 'description']

    def create(self, validated_data):
        zip_code_pick_up = validated_data.pop('zip_code_pick_up')
        zip_code_delivery = validated_data.pop('zip_code_delivery')

        pick_up_location = Location.objects.filter(zip_code=zip_code_pick_up).first()
        delivery_location = Location.objects.filter(zip_code=zip_code_delivery).last()

        if not pick_up_location or not delivery_location:
            raise serializers.ValidationError({'error': 'Invalid zip_code'})

        validated_data['pick_up_location'] = pick_up_location
        validated_data['delivery_location'] = delivery_location

        return super().create(validated_data)


class CargoListSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.SerializerMethodField()
    delivery_location = serializers.SerializerMethodField()
    nearest_car_count = serializers.SerializerMethodField()

    @staticmethod
    def get_pick_up_location(cargo):
        return cargo.pick_up_location.zip_code

    @staticmethod
    def get_delivery_location(cargo):
        return cargo.delivery_location.zip_code

    @staticmethod
    def get_nearest_car_count(cargo):
        cargo_location = (cargo.pick_up_location.latitude, cargo.pick_up_location.longitude)
        car_locations = Location.objects.exclude(car=None).values_list('latitude', 'longitude')
        nearest_car_count = 0

        for car_location in car_locations:
            car_distance = distance(cargo_location, car_location).miles
            if car_distance <= 450:
                nearest_car_count += 1

        return nearest_car_count

    class Meta:
        model = Cargo
        fields = ['pick_up_location', 'delivery_location', 'nearest_car_count']
