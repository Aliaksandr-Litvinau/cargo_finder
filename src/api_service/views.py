from rest_framework import generics

from api_service.models import Cargo, Car
from api_service.serializers import CargoSerializer, CargoListSerializer, CargoDetailSerializer, CarSerializer


class CargoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoListAPIView(generics.ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoListSerializer


class CargoDetailAPIView(generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoDetailSerializer


class CarUpdateAPIView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'car_id'


