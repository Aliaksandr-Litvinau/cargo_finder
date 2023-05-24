from django.urls import path

from api_service.views import CargoListCreateAPIView, CargoListAPIView

urlpatterns = [
    path('cargo/create/', CargoListCreateAPIView.as_view(), name='cargo-create'),
    path('cargo/', CargoListAPIView.as_view(), name='cargo-list'),
]
