from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/',  views.register , name='register'),
    path('login/',  views.login , name='login'),
    path('logout/',  views.login , name='logout'),

    #these shoul go to repective app on phase 2
    path('home/',  views.home , name='home'),
    path('modules/',  views.modules , name='modules'),
    path('single-module/',  views.single_module , name='single_module'),
    path('welcome/',  views.welcome , name='welcome'),
    path('live-discussion/',  views.live_discussion , name='live_discussion'),
]