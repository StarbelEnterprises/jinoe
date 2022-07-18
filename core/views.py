from multiprocessing import context
from django.shortcuts import render

from core.models import Enrollment

# Create your views here.
def welcome(request):
    query_set = Enrollment.objects.filter(student=request.user)

    enrolled_level = Enrollment.objects.filter(student=request.user).first()
    print(enrolled_level.level.name)
    print(enrolled_level.level.get_modules())  
    context={
        'enrolled_level':  enrolled_level,
        'modules': enrolled_level.level.get_modules()
    }
    return render(request, 'dashboard/welcome.html', context=context)

