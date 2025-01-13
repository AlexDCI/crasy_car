from django.urls import path
from users.views import login_user, logout_user
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('login/',login_user, name='login'), 
    path('logout/',logout_user, name='logout'), 
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)