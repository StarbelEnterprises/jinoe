from django.contrib import admin
from . models import *

admin.site.site_header = 'Jinoe Admin'

class EnrolledEductionLevel(admin.StackedInline):
    model = CariculamEnrollment
    extra = 0 

@admin.register(CariculamLevels)
class EductionLevels(admin.ModelAdmin):
    onlines:(EnrolledEductionLevel)
admin.site.register(CariculamEnrollment)
admin.site.register(CariculamModules)
admin.site.register(CariculamSubjects)


admin.site.register(CariculamSubLevelSet)
admin.site.register(CariculamSubLevelEntry)

class SubSubTopicInline(admin.StackedInline):
    model = CariculamSubSubTopic
    extra = 2

class SubSubTopicVideosInline(admin.StackedInline):
    model = CariculamSubSubTopicVideos
    extra = 2

class SubTopicVideosInline(admin.StackedInline):
    model = CariculamSubTopicVideos
    extra = 2


class SubTopicsAdmin(admin.ModelAdmin): 
    inlines = [
        SubSubTopicInline,SubTopicVideosInline,
    ]

class SubSubTopicAdmin(admin.ModelAdmin):
    inlines = [SubSubTopicVideosInline,]


class TopicVideosInline(admin.StackedInline):
    model = CariculamTopicVideos
    extra = 2

class TopicsAdmin(admin.ModelAdmin):
    inlines = [TopicVideosInline,]

# class SubTopicAdmin(admin.ModelAdmin):
#     inlines = [SubTopicVideosInline]


admin.site.register(CariculamSubTopics,SubTopicsAdmin)
admin.site.register(CariculamTopics,TopicsAdmin)
admin.site.register(CariculamSubSubTopic,SubSubTopicAdmin)
