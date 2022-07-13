from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/',  views.login , name='login'),
    path('register/',  views.register , name='register'),
    path('logout/',  views.login , name='logout'),



    path('home/',  views.home , name='home'),
    path('modules/',  views.modules , name='modules'),
    path('welcome/',  views.welcome , name='welcome'),
    path('live-discussion/',  views.live_discussion , name='live_discussion'),
]