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
