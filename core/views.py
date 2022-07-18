from multiprocessing import context
from django.shortcuts import render

from core.models import Enrollment

# Create your views here.
def welcome(request):
    query_set = Enrollment.objects.filter(student=request.user)
    context={
        'enrollment': query_set,
        'modules': query_set.get_enrolled_modules()
    }
    return render(request, 'dashboard/welcome.html', context=context)

