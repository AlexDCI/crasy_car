# Generated by Django 5.0.3 on 2024-04-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
