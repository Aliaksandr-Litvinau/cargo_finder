from rest_framework import generics

from api_service.models import Cargo
from api_service.serializers import CargoSerializer


class CargoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
