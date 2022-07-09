
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from enum import Enum

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
        verbose_name_plural = 'Level Modules'
        db_table = 'jinoe_level_modules'
     
    def __str__(self):
        return  str(self.name)

class Subjects(models.Model):
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=True,blank=True)
    subject_type = models.CharField(max_length=60, null=True,blank=True)
    STATUS_CHOICES = (
    ('ST', 'STARTED'),
    ('NST', 'NOT_STARTED'),
    ('DL', 'DELAYED'),
    ('CMP', 'COMPLETED'),
    ('DISC', 'DISQUALIFIED'),
)
    progress_status = models.CharField(max_length=30, null=False,blank=False,choices=STATUS_CHOICES)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sbj_created_by', null=True)


    class Meta:
        verbose_name_plural = 'Module Subjects'
        db_table = 'jinoe_module_subjects'    
    
    def __str__(self):
        return str(self.name)

class Topics(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=True,blank=True)
    STATUS_CHOICES = (
    ('ST', 'STARTED'),
    ('NST', 'NOT_STARTED'),
    ('DL', 'DELAYED'),
    ('CMP', 'COMPLETED'),
    ('DISC', 'DISQUALIFIED'),
)
    topic_status = models.CharField(max_length=30,choices=STATUS_CHOICES,null=False,blank=False)
    media = models.CharField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'Subject topics'
        db_table = 'jinoe_subject_topics'    
    
    def __str__(self):
        return str(self.name)






# class Subjects(models.model):
    


