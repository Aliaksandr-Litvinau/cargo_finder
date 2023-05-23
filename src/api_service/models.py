from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.city}, {self.state} {self.zip_code}"


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pick_up_cargos')
    delivery_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='delivery_cargos')
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()

    def __str__(self):
        return f"Cargo #{self.pk}"


class Car(models.Model):
    unique_number_regex = r'^[1-9]\d{3}[A-Z]$'
    unique_number_validator = RegexValidator(
        regex=unique_number_regex,
        message='Unique number must be in the format of 4 digits followed by one uppercase letter.'
    )
    unique_number = models.CharField(
        max_length=5,
        unique=True,
        validators=[unique_number_validator]
    )
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    carrying_capacity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def __str__(self):
        return f"Car {self.unique_number}"
