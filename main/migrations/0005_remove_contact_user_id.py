# Generated by Django 5.0.3 on 2024-04-25 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
    ]
