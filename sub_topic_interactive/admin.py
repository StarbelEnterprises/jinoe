from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(SubTopicQuestions)
admin.site.register(SubTopicAnswerOptions)
admin.site.register(SubTopicAnswerLogs)
admin.site.register(SubTopicLikes)
admin.site.register(SubTopicRates)