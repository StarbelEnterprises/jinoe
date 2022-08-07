
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from core.models import Chapter, Enrollment, Modules, SubSubTopic, SubTopics, Topics
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core import serializers



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


class ModuleDetails(View):
    def get(self, request, pk, *args, **argus):
        module =  Modules.objects.get(pk=pk)
       
        context = {
        'module': module
        }

        return render(request, template_name='dashboard/module_single.html',context=context)

    def post(self, request, pk, *args, **argus):
        print( request.POST.get('id'))
        subtopic = get_object_or_404(SubTopics, id=request.POST.get('id'))
        subsubtopic = serializers.serialize("json", SubSubTopic.objects.filter(sub_sub_topic_id=subtopic))
    
        
    
        response = {
            'success': 'true',
            'data':subsubtopic,
            'msg': f' we can get some data'}
        return JsonResponse(response, safe= False)



class CurriculumDetails(View):
    def get(self, request, pk, *args, **argus):
        module =  Modules.objects.get(pk=pk)
       
        context = {
        'module': module
        }

        return render(request, template_name='curriculum/module_single.html',context=context)

    def post(self, request, pk, *args, **argus):
        print( request.POST.get('id'))
        subtopic = get_object_or_404(SubTopics, id=request.POST.get('id'))
        subsubtopic = serializers.serialize("json", SubSubTopic.objects.filter(sub_sub_topic_id=subtopic))
    
        
    
        response = {
            'success': 'true',
            'data':subsubtopic,
            'msg': f' we can get some data'}
        return JsonResponse(response, safe= False)
