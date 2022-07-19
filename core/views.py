from multiprocessing import context
from django.shortcuts import render

from core.models import Enrollment
from django.core.paginator import Paginator


# Create your views here.
def welcome(request):
    query_set = Enrollment.objects.filter(student=request.user)

    enrolled_level = Enrollment.objects.filter(student=request.user).first()
    enrolled_modules = enrolled_level.level.get_modules()

    # paginate the modules
    paginator = Paginator(enrolled_modules, 7) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    paginated_module_obj = paginator.get_page(page_number)
    for mod in paginated_module_obj:
        print(mod.get_core_offer_module)

    context={
        'enrolled_level':  enrolled_level,
        'modules': paginated_module_obj
    }
    return render(request, 'dashboard/welcome.html', context=context)

