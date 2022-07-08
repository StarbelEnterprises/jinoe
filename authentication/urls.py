import imp
from django.urls import path
from .  import views 

urlpatterns = [
    # login
    # register
    # logout
    path('',  views.index , name='index'),
    
]