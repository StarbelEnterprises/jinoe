from django.contrib import admin
from authentication.models import *

admin.site.register(Experience)
admin.site.register(Certificate)
admin.site.register(EducationBacbackground)
admin.site.register(Skills)

@admin.register(UserProfile)
class ClassesAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'create_at',  'updated_at',)
    list_display_links = ('user',)
    search_fields = ('about', 'user__username')
    ordering = ['id', 'create_at']
    list_per_page = 10
  