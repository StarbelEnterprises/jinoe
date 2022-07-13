from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Questions)
admin.site.register(AnswerOptions)
admin.site.register(AnswerLogs)
admin.site.register(TopicLikes)
admin.site.register(TopicRates)

