from django.shortcuts import render
from core.models import Enrollment
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@login_required(login_url='login')
def welcome(request):
    try:
        enrolled_level = Enrollment.objects.filter(student=request.user).first()
        if enrolled_level is not None:
            enrolled_modules = enrolled_level.level.get_modules() 

            # paginate the modules
            paginator = Paginator(enrolled_modules, 7) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            paginated_module_obj = paginator.get_page(page_number)
            context = {
                'enrolled_level': enrolled_level,
                'modules': paginated_module_obj
            }
            return render(request, 'dashboard/welcome.html', context=context)
            # put some massage
        return render(request, 'dashboard/welcome.html',)
    except ObjectDoesNotExist:
        raise 

