from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.decorators import login_required


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, password=None, **extra_fields):
        if not first_name:
            raise ValueError('Имя обязательно')
        user = self.model(first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(first_name, password, **extra_fields)
    
    def get_by_natural_key(self, username):
        return self.get(first_name=username)



# @login_required(login_url='/users/login/')
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    seller_or_buyer = models.CharField(max_length=4, choices=[('SELL', 'seller'), ('BUY', 'buyer')])
    sing_up_data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()
    
    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['last_name', 'email', 'birth_date', 'seller_or_buyer']

    def clean(self):
            from datetime import date
            if (date.today() - self.birth_date).days < 365 * 18:
                raise ValidationError(_('age should be not lass as 18'))
            
    def __str__(self) -> str:
         return f'{self.first_name} {self.last_name}'




class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    model_car = models.CharField(max_length=150)
    color_car = models.CharField(max_length=50)
    relise_data = models.DateField()
    motor_type = models.CharField(max_length=50, choices=[('BENZZIN', 'benzzin'), ('DISEL', 'disel'), ('GAS', 'gas'), ('ELECTRO', 'electro')])
    motor_power = models.FloatField()
    prise = models.DecimalField(max_digits=10, decimal_places=2)
    description_car = models.TextField(blank=True)

    # def __str__(self) -> str:
    #      return f'{self.owner}' # {self.model_car} {self.color_car} {self.relise_data} {self.motor_type} {self.motor_power} {self.prise} {self.description_car}'


class Example(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()


class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     subject = models.CharField(max_length=350)
     message = models.TextField()