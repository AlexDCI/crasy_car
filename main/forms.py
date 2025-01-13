from django import forms
from main.models import User, Car, Contact
from django.contrib.auth.hashers import make_password




class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'birth_date', 'seller_or_buyer']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Хешируем пароль
        if commit:
            user.save()
        return user




class RegisterCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['owner', 'model_car', 'color_car', 'relise_data', 'motor_type', 'motor_power', 'prise', 'description_car']
        labels = {
            'model_car': 'Write car model',
            'color_car': 'Write car color',
            'relise_data': 'Write car release date',
            'motor_type': 'Choose motor type',
            'motor_power': 'Write engine capacity',
            'prise': 'Write car price',
            'description_car': 'Describe your car'
        }


class SearchCarForm(forms.Form):
    model_car = forms.CharField(required=False)
    color_car = forms.CharField(required=False)
    relise_data = forms.DateField(required=False)
    motor_type = forms.CharField(required=False)
    prise = forms.DecimalField(required=False)

    def search(self):
        # Инициализация QuerySet
        queryset = Car.objects.all()

        # Фильтрация по полям формы
        if self.cleaned_data.get('model_car'):
            queryset = queryset.filter(model_car=self.cleaned_data['model_car'])
        if self.cleaned_data.get('color_car'):
            queryset = queryset.filter(color_car=self.cleaned_data['color_car'])
        if self.cleaned_data.get('relise_data'):
            queryset = queryset.filter(relise_data=self.cleaned_data['relise_data'])
        if self.cleaned_data.get('motor_type'):
            queryset = queryset.filter(motor_type=self.cleaned_data['motor_type'])
        if self.cleaned_data.get('prise'):
            queryset = queryset.filter(prise=self.cleaned_data['prise'])

        return queryset
        



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

