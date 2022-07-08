from re import T
from tabnanny import verbose
from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Audit(models.Model):
    create_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

   
class UserProfile(Audit):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    second_name = models.CharField(max_length=60, null=True, blank=True)
    about = models.TextField(null=True, blank=  True)

    class Meta:
        verbose_name_plural = 'User profile'
        db_table = 'jinoe_user_profile'
     
    def __str__(self):
        return  self.user.first_name



    
