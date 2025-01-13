from django.contrib.auth.hashers import make_password
from main.models import User
from django.core.management.base import BaseCommand

def migrate_passwords():
    users = User.objects.all()
    for user in users:
        user.password = make_password(user.password)
        user.save()


class Command(BaseCommand):
    help = 'Migrates passwords to hashed values'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            user.password = make_password(user.password)
            user.save()
        self.stdout.write(self.style.SUCCESS('Passwords migrated successfully'))