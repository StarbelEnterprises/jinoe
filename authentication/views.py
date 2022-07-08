from django.shortcuts import render
from . models import UserProfile

# Create your views here.
def index(request):
    query  = UserProfile.objects.all()
    context_data = {
        'user_profile': query
    }

    return render(request, template_name='auth/user_profile.html', context= context_data)