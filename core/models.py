
from sys import stdout
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from enum import Enum
from django.utils.translation import gettext_lazy as _

class Levels(models.Model):
    order_by = models.IntegerField(null=True,)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    name = models.CharField(max_length=60, null= True , blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)
    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lv_created_by', null=True)


    class Meta:
        verbose_name_plural = 'Eduction Levels'
        db_table = 'jinoe_user_Levels'
     
    def __str__(self):
        return  str(self.name)

class Enrollment(models.Model):
    level = models.ForeignKey(Levels, on_delete=models.CASCADE, related_name='enrolled_to_set')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_student_set')
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrol_created_by', null=True)
    class Meta:
        verbose_name_plural = 'Enrolled Education level'
        db_table = 'jinoe_enrolled_eduction_level'
     
    def __str__(self):
        return  f'{self.student.username} enrolled to {self.level.name}'

class Modules(models.Model):
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    name = models.CharField(max_length= 60, null= True, blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)
    
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

    class SubjectsProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    progress_status = models.CharField(max_length=30,choices=SubjectsProgressStatuses.choices,default=SubjectsProgressStatuses.NOT_STARTED,)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sbj_created_by', null=True)


    class Meta:
        verbose_name_plural = 'Module Subjects'
        db_table = 'jinoe_module_subjects'    
    
    def __str__(self):
        return str(self.name)

class Topics(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=True,blank=True)

    class TopicsProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    topic_status = models.CharField(max_length=30,choices=TopicsProgressStatuses.choices,default=TopicsProgressStatuses.NOT_STARTED,)
    media = models.CharField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'Subject Topics'
        db_table = 'jinoe_subject_topics'    
    
    def __str__(self):
        return str(self.name)

class SubTopics(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=True,blank=True)

    class SubTopicsProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    sub_topic_status = models.CharField(max_length=30,choices=SubTopicsProgressStatuses.choices,default=SubTopicsProgressStatuses.NOT_STARTED,)
    media = models.CharField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Subtopics'
        db_table = 'jinoe_topic_subtopics'    
    
    def __str__(self):
        return str(self.name)

    


