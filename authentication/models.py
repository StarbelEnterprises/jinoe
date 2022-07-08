from concurrent.futures.process import _ThreadWakeup
from datetime import datetime, timezone

from re import T
from tabnanny import verbose
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
from django.db import models
from django.contrib.auth.models import User

   
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    about = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin', null=True)

    class Meta:
        verbose_name_plural = 'User profile'
        db_table = 'jinoe_user_profile'
     
    def __str__(self):
        return  str(self.user.first_name)

    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
       UserProfile.objects.create(user=instance)
    instance.userprofile.save()



    
