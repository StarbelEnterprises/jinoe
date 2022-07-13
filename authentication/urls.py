from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/',  views.login , name='login'),
    path('home/',  views.home , name='home'),
    path('register/',  views.register , name='register'),
    path('logout/',  views.login , name='logout'),
    
]