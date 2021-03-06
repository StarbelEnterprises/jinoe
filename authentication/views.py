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
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(' it works bus something is wrong')
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {username}.")
                return redirect("welcome")
            else:
                print('user no exists')
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

            print('something')
            return render(request, template_name='auth/login.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        eductional_level = Levels.objects.all().order_by('order_by')
        context ={
        'eduction_levels': eductional_level
        }
        return render(request, template_name='auth/register.html', context=context)
    def post(self, request, *args, **kwargs):
        post_data = request.POST
        pp.pprint(post_data)
        username = post_data.get('username')
        first_name =post_data.get('firstname')
        last_name = post_data.get('lastname')
        email =post_data.get('email')
        password = post_data.get('password1')
        enrolled_level = post_data.get('enrolled_to')
       
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


def logout_user(request):
	logout(request)
	return redirect("welcome")      

