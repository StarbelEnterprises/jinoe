from django.shortcuts import render
from . models import UserProfile

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')


def modules(request):
    return render(request, template_name='dashboard/modules.html')

def single_module(request):
    return render(request, template_name='dashboard/module_single.html')

def welcome(request):
    return render(request, 'dashboard/welcome.html')



def live_discussion(request):
    return render(request, 'dashboard/live_discussion.html')

def carrer_profile(request):
    return render(request, 'dashboard/carrer_entry_profile.html')


def forum(request):
    return render(request, 'dashboard/forum.html')




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