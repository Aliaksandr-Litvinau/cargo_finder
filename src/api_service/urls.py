from django.urls import path

from api_service.views import \
    CargoListCreateAPIView, \
    CargoListAPIView, \
    CargoDetailAPIView, \
    CarUpdateAPIView, \
    CargoUpdateAPIView

urlpatterns = [
    path('cargo/create/', CargoListCreateAPIView.as_view(), name='cargo-create'),
    path('cargo/', CargoListAPIView.as_view(), name='cargo-list'),
    path('cargo/<int:pk>/', CargoDetailAPIView.as_view(), name='cargo-detail'),
    path('cargo/<cargo_id>/update/', CargoUpdateAPIView.as_view(), name='cargo-update'),
    path('cars/<int:car_id>/update/', CarUpdateAPIView.as_view(), name='car-update'),
]

