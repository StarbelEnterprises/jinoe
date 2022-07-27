from django.contrib import admin
from . models import *

class EnrolledEductionLevel(admin.StackedInline):
    model = Enrollment
    extra = 0  # how many rows to show

@admin.register(Levels)
class EductionLevels(admin.ModelAdmin):
    onlines:(EnrolledEductionLevel)
admin.site.register(Enrollment)
admin.site.register(Modules)
admin.site.register(Subjects)
admin.site.register(Topics)
admin.site.register(SubTopics)
# admin.site.register(SubLevelSet)
# admin.site.register(SubLevelEntry)
