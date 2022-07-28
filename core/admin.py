from django.contrib import admin
from . models import *

admin.site.site_header = 'Jinoe Admin'

class EnrolledEductionLevel(admin.StackedInline):
    model = Enrollment
    extra = 0  # how many rows to show

@admin.register(Levels)
class EductionLevels(admin.ModelAdmin):
    onlines:(EnrolledEductionLevel)
admin.site.register(Enrollment)
admin.site.register(Modules)
admin.site.register(Chapter)
admin.site.register(Topics)

admin.site.register(SubLevelSet)
admin.site.register(SubLevelEntry)

class SubSubTopicInline(admin.StackedInline):
    model = SubSubTopic
    extra = 2


class SubTopicsAdmin(admin.ModelAdmin): 
    inlines = [
        SubSubTopicInline,
    ]

admin.site.register(SubTopics,SubTopicsAdmin)
