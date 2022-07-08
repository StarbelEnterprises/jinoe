
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile

class Levels(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    name = models.CharField(max_length=60, null= True , blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lv_created_by', null=True)


    class Meta:
        verbose_name_plural = 'user Levels'
        db_table = 'jinoe_user_Levels'
     
    def __str__(self):
        return  str(self.name)

class Modules(models.Model):
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    name = models.CharField(max_length= 60, null= True, blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='md_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Modules'
        db_table = 'jinoe_user_modules'
     
    def __str__(self):
        return  str(self.name)

# class Subjects(models.model):
    



