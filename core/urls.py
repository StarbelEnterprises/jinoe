from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',  views.welcome , name='welcome'),
    path('single-module/<int:pk>',  views.ModuleDetails.as_view() , name='single_module'),
    path('landing/',  views.landing, name='landing'),

]