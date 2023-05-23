# Generated by Django 4.0 on 2023-05-23 18:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('description', models.TextField()),
                ('delivery_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_cargos', to='api_service.location')),
                ('pick_up_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_cargos', to='api_service.location')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_number', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator(message='Unique number must be in the format of 4 digits followed by one uppercase letter.', regex='^[1-9]\\d{3}[A-Z]$')])),
                ('carrying_capacity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_service.location')),
            ],
        ),
    ]