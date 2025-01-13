from django.urls import path
from main.views import main_page, base_page, feedback, register_car, register_user, example, review_page, get_weather #, get_car_news
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page, name='main'),
    path('sell/', register_car, name='sell_car'),
    path('feedback/', feedback, name='feedback'),
    path('base/', base_page, name='base'),
    path('registration/', register_user, name='registration'),
    path('example/', example, name='example'),
    path('review/', review_page, name='review'),
    #path('news/', get_car_news, name='news'),
    path('weather/', get_weather, name='weather'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)