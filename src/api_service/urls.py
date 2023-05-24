from django.urls import path

from api_service.views import CargoListCreateAPIView

urlpatterns = [
    path('cargo/create/', CargoListCreateAPIView.as_view(), name='cargo-create'),
]
