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
# admin.site.register(Topics)

admin.site.register(SubLevelSet)
admin.site.register(SubLevelEntry)

class SubSubTopicInline(admin.StackedInline):
    model = SubSubTopic
    extra = 2

class SubSubTopicVideosInline(admin.StackedInline):
    model = SubSubTopicVideos
    extra = 2

class SubTopicVideosInline(admin.StackedInline):
    model = SubTopicVideos
    extra = 2


class SubTopicsAdmin(admin.ModelAdmin): 
    inlines = [
        SubSubTopicInline,SubTopicVideosInline,
    ]

class SubSubTopicAdmin(admin.ModelAdmin):
    inlines = [SubSubTopicVideosInline,]


class TopicVideosInline(admin.StackedInline):
    model = TopicVideos
    extra = 2

class TopicsAdmin(admin.ModelAdmin):
    inlines = [TopicVideosInline,]

# class SubTopicAdmin(admin.ModelAdmin):
#     inlines = [SubTopicVideosInline]


admin.site.register(SubTopics,SubTopicsAdmin)
admin.site.register(Topics,TopicsAdmin)
# admin.site.register(SubTopics,SubTopicAdmin)
admin.site.register(SubSubTopic,SubSubTopicAdmin)