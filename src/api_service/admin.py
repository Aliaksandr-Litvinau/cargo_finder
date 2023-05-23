from django.contrib import admin

from api_service.models import Location, Cargo, Car


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields]


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cargo._meta.fields]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
