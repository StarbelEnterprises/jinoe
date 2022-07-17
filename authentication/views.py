from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
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


def webinar(request):
    return render(request, 'dashboard/webinar.html')

def landing(request):
    return render(request, template_name='auth/landing.html')
    
def login(request):
    #login logic    
    return render(request, template_name='auth/login.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='auth/register.html')
    def post(self, request, *args, **kwargs):
        response = {
        'success': 'true',
        'msg': f' You have done request'}
        return JsonResponse(response)

def Logout(request):
    # logout logic
    return render(request, template_name='auth/logout.html')