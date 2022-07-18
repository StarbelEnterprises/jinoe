from django.contrib import admin
from . models import *

class EnrolledEductionLevel(admin.TabularInline):
    model = Enrollment
    extra = 5 # how many rows to show

@admin.register(Levels)
class EductionLevels(admin.ModelAdmin):
    inlines:(EnrolledEductionLevel)
admin.site.register(Enrollment)
admin.site.register(Modules)
admin.site.register(Subjects)
admin.site.register(Topics)
admin.site.register(SubTopics)