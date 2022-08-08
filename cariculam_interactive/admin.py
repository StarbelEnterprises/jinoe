from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(CariculamQuestions)
admin.site.register(CariculamAnswerOptions)
admin.site.register(CariculamAnswerLogs)
admin.site.register(CariculamTopicLikes)
admin.site.register(CariculamTopicRates)