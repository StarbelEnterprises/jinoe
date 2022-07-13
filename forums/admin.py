from django.contrib import admin
from . models import *

admin.site.register(Discussion)
admin.site.register(DiscussionLikes)
admin.site.register(DiscussionReply)

