from django.shortcuts import render, redirect
from main.forms import RegisterUser, RegisterCar, ContactForm, SearchCarForm
from main.models import User, Car, Contact
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import requests

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



def autorisation(request, page, back_page):
    form = ContactForm(request.POST or None)
    if request.user.is_anonymous and request.method == 'POST':
        return redirect(page)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request,  back_page, context=context)



def main_page(request):
    return autorisation(request, '/users/login/', 'main/main.html')
   


def base_page(request):
    context = {}
    return render(request, 'base.html', context=context)


def sell_car(request):
    form = RegisterCar()
    return render(request, 'main/sell_car.html', {'form': form})


def feedback(request):
    message = {'message': Contact.objects.all()}
    return render(request, 'main/feedback.html', context=message)


def register_user(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('main')
    else:
        form = RegisterUser()
    return render(request, 'main/registration.html', {'form': form})


@login_required(login_url='/users/login/')
def register_car(request):
    current_user = request.user
    data = {'data': User.objects.all(), 'current_user': current_user}
    if request.method == 'POST':
        form = RegisterCar(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('main')
    else:
        form = RegisterCar()
    return render(request, 'main/sell_car.html', context=data) 



from main.form_example import AddExampleForm

def example(request):
    if request.method == 'POST':
        form = AddExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AddExampleForm()
    context = {
        'title': 'Regestr here',
        'form': form
    }
    return render(request, 'main/example.html', context=context)


def review_page(request):
    if request.method == 'POST':
        if request.user.is_anonymous:
            return autorisation(request, '/users/login/', 'main/main.html')
        form = SearchCarForm(request.POST)
        if form.is_valid():
            model_car = form.cleaned_data.get('model_car')
            color_car = form.cleaned_data.get('color_car')
            relise_data = form.cleaned_data.get('relise_data')
            motor_type = form.cleaned_data.get('motor_type')
            prise = form.cleaned_data.get('prise')

            # Формируем условия для поиска по модели и хотя бы одному параметру
            condition = Q(model_car=model_car)
            if color_car:
                condition |= Q(color_car=color_car)
            if relise_data:
                condition |= Q(relise_data=relise_data)
            if motor_type:
                condition |= Q(motor_type=motor_type)
            if prise:
                condition |= Q(prise=prise)

            # Ищем автомобили, удовлетворяющие условиям
            cars = Car.objects.filter(condition)
            return render(request, 'main/review.html', {'form': form, 'cars': cars})
    else:
        form = SearchCarForm()
    return render(request, 'main/review.html', {'form': form, 'cars': None})



# API FUNCTIONS

# @login_required(login_url='/users/login/')
# def get_car_news(request):
#     api_key = '291294620d95e4d85130fa27bc0d7d5f'
#     url = 'https://gnews.io/api/v4/search?q=car&lang=en&country=us&max=10&apikey=' + api_key

#     try:
#         response = requests.get(url)
#         news_data = response.json().get('articles', [])
#         return render(request, 'main/api_news.html', {'news_data': news_data})
#     except Exception as e:
#         error_message = str(e)
#         return render(request, 'main/api_news.html', {'error_message': error_message})


def get_weather(request):
    owm = OWM('ca691c0a077b7441f179a898670138e2')
    mgr = owm.weather_manager()
    # Search for current weather in Rostok, Germany and get details
    observation = mgr.weather_at_place('Rostok,DE')
    weather = observation.weather
    context = {
        'temperature': weather.temperature('celsius').get('temp'),
        'clouds': weather.clouds
    }
    return render(request, 'main/weather.html', context)
