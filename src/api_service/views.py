from rest_framework import generics

from api_service.models import Cargo
from api_service.serializers import CargoSerializer, CargoListSerializer, CargoDetailSerializer


class CargoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoListAPIView(generics.ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoListSerializer


class CargoDetailAPIView(generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoDetailSerializer


