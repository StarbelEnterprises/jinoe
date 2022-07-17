import email
from urllib import request
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from core.models import Enrollment, Levels
from . models import UserProfile
from django.contrib.auth.models import User

import pprint
pp = pprint.PrettyPrinter(indent=4)



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
    
class Login(View):
    def get(self, request,*args, **kwargs):
        form = AuthenticationForm()
        return render(request, template_name='auth/login.html', context={'login_form': form} )


    def post(self, request, *args, **kwags):
        form = AuthenticationForm(request, data=request.POST)
        pp.pprint(form.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {username}.")
                return redirect("welcome")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        
        return render(request, template_name='auth/login.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        eductional_level = Levels.objects.all().order_by('order_by')
        context ={
        'eduction_levels': eductional_level
        }
        return render(request, template_name='auth/register.html', context=context)
    def post(self, request, *args, **kwargs):
        pp.pprint(request.POST)
        post_data = request.POST
        username = post_data.get('username')
        first_name =post_data.get('firstname')
        last_name = post_data.get('lastname')
        email =post_data.get('email')
        password = post_data.get('password')
        enrolled_level = post_data.get('enrolled_to[id]')
       
        if not (User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
            User.objects.create_user(
                username, email, password=password, first_name=first_name, last_name=last_name,  is_active=True)
            # it going to be used later in the email sending
            _user = User.objects.get(username=username, email=email)
            # TODO send email address to activate a user if you want it to

            # save enrolled levels
            _level = Levels.objects.get(id=enrolled_level)
            _enrollment, create = Enrollment.objects.get_or_create(level=_level, student=_user)

            pp.pprint(_user)
            response = {
            'success': 'true',
            'msg': f' You have done request'}
            return JsonResponse(response)
        else:
            response = {
            'success': 'true',
            'msg': f' User exists'}
            return JsonResponse(response)

       

def Logout(request):
    # logout logic
    return render(request, template_name='auth/logout.html')