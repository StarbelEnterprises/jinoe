from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',  views.welcome , name='welcome'),
    path('single-module/',  views.single_module , name='single_module'),
]