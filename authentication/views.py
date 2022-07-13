from django.shortcuts import render
from . models import UserProfile

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')
def landing(request):
    return render(request, template_name='auth/landing.html')
    
def login(request):
    #login logic    
    return render(request, template_name='auth/login.html')

def register(request):
    # register logic
    return render(request, template_name='auth/register.html')

def Logout(request):
    # logout logic
    return render(request, template_name='auth/logout.html')