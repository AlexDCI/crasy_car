# Generated by Django 5.0.3 on 2024-04-21 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('seller_or_buyer', models.CharField(choices=[('SELL', 'seller'), ('BUY', 'buyer')], max_length=4)),
                ('sing_up_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_car', models.CharField(max_length=150)),
                ('color_car', models.CharField(max_length=50)),
                ('relise_data', models.DateField()),
                ('motor_type', models.CharField(choices=[('BENZZIN', 'benzzin'), ('DISEL', 'disel'), ('GAS', 'gas'), ('ELECTRO', 'electro')], max_length=50)),
                ('motor_power', models.FloatField()),
                ('prise', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description_car', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='main.user')),
            ],
        ),
    ]