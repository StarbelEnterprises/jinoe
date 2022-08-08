
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from cariculam_core.models import CariculamSubjects
from core.models import Chapter, Enrollment, Modules, SubSubTopic, SubTopics, Topics
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core import serializers


class CurriculumDetails(View):
    def get(self, request, pk, *args, **argus):
        subject =  CariculamSubjects.objects.get(pk=pk)
        curriculum_level = Enrollment.objects.filter(student=request.user).first()
        enrolled_curruculum = curriculum_level.level.get_currilum() 
        context = {
        'module': subject,
        'enrolled_subjects':  enrolled_curruculum
        }
        return render(request, template_name='curriculum/module_single.html', context=context)

    def post(self, request, pk, *args, **argus):
        subtopic = get_object_or_404(SubTopics, id=request.POST.get('id'))
        subsubtopic = serializers.serialize("json", SubSubTopic.objects.filter(sub_sub_topic_id=subtopic))
        response = {
            'success': 'true',
            'data':subsubtopic,
            'msg': f' we can get some data'}
        return JsonResponse(response, safe= False)
