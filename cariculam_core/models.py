
from pyexpat import model
import re
from sys import stdout
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from enum import Enum
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class CariculamLevels(models.Model):
    order_by = models.IntegerField(null=True,)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    name = models.CharField(max_length=60, null= True , blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clv_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Levels'
        db_table = 'jinoe_cariculam_user_Levels'
     
    def __str__(self):
        return  str(self.name)

    def get_modules(self):
        return self.module_set.all().order_by('order_by')

class CariculamEnrollment(models.Model):
    level = models.ForeignKey(CariculamLevels, on_delete=models.CASCADE, related_name='c_enrolled_to_set')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_enrolled_student_set')
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_enrol_created_by', null=True)
    class Meta:
        verbose_name_plural = 'Enrolled Cariculam level'
        db_table = 'jinoe_enrolled_cariculam_eduction_level'
     
    def __str__(self):
        
        return  f'{self.student.username} enrolled to {self.level.name}'

class CariculamSubLevelSet(models.Model):
    sub_level_set_level_id = models.ForeignKey(CariculamLevels,on_delete=models.CASCADE,related_name="c_sub_level_set_level_id_col")
    name = models.CharField(max_length=60,null=False,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_stlv_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Sub Level Sets'
        db_table = 'jinoe_cariculam_sub_level_set'
     
    def __str__(self):
        return  str(self.name)
    
    # @receiver(post_save, sender=Levels)
    # def create_or_update_sub_level_set(sender, instance, created, **kwargs):
    #     if created:
    #         SubLevelSet.objects.create(sub_level_set_level_id=instance)

class CariculamSubLevelEntry(models.Model):
    sub_level_entry_set_id = models.ForeignKey(CariculamSubLevelSet,on_delete=models.CASCADE,related_name="c_sub_level_entry_set_id_col")
    name = models.CharField(max_length=60,null=False,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_stlv_entry_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Sub Level Set Elements'
        db_table = 'jinoe_cariculam_sub_level_set_elements'
     
    def __str__(self):
        return  str(self.name)

    # @receiver(post_save, sender=SubLevelSet)
    # def create_or_update_sub_level_set_entry(sender, instance, created, **kwargs):
    #     if created:
    #         SubLevelEntry.objects.create(sub_level_elem_set_id=instance)
   
class CariculamModules(models.Model):
    MODULE_TYPE = (
        ('normal', 'normal module'),
        ('core', 'core module'),
        )
    module_type = models.CharField(max_length=200,null=True, blank=False, choices=MODULE_TYPE)
    class ModuleProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    progress_status = models.CharField(max_length=30,choices=ModuleProgressStatuses.choices,default=ModuleProgressStatuses.NOT_STARTED,)
    module_Level_id = models.ForeignKey(CariculamLevels, on_delete=models.CASCADE, related_name='c_module_set',default=0)
    name = models.CharField(max_length= 60, null= True, blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    description = models.TextField(null=True, blank=False)
    order_by = models.IntegerField(null=True, blank=False)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_md_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Level Modules'
        db_table = 'jinoe_cariculam_level_modules'
     
    def __str__(self):
        print(self.module_type == 'cariculam_core')
        return  str(self.name)

    @property
    def get_core_offer_module(self):
        return self.module_type == 'cariculam_core'

class CariculamSubjects(models.Model):
    module_subject_id = models.ForeignKey(CariculamModules, on_delete=models.CASCADE,related_name="c_module_subject_id_col",default=0)
    name = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_sbj_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Module Subjects'
        db_table = 'jinoe_cariculam_module_subjects'    
    
    def __str__(self):
        return f'[Module-] {self. module_chapter_id.name}--{self.name}'

class CariculamTopics(models.Model):
    topic_subject_id = models.ForeignKey(CariculamSubjects, on_delete=models.CASCADE,related_name="c_topic_subject_id_col",default=0)
    name = models.CharField(max_length=60,null=True,blank=True)

    class TopicsProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    topic_status = models.CharField(max_length=30,choices=TopicsProgressStatuses.choices,default=TopicsProgressStatuses.NOT_STARTED,)
    media = models.FileField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_topic_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'Cariculam Module Topics'
        db_table = 'jinoe_cariculam_subject_topics'    
    
    def __str__(self):
        return f'{self.topic_chapter_id}--{self.name}'

class CariculamSubTopics(models.Model):
    sub_tipic_topic_id = models.ForeignKey(CariculamTopics, on_delete=models.CASCADE,related_name="c_sub_tipic_topic_id_col",default=0)
    sub_topic_name = models.CharField(max_length=60,null=True,blank=True)

    class SubTopicsProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    sub_topic_status = models.CharField(max_length=30,choices=SubTopicsProgressStatuses.choices,default=SubTopicsProgressStatuses.NOT_STARTED,)
    sub_tipic_media = models.FileField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Topic Subtopics'
        db_table = 'jinoe_cariculam_topic_subtopics'    
    
    def __str__(self):
        return f'{self.sub_tipic_topic_id.name}-->{self.sub_topic_name}'

class CariculamSubSubTopic(models.Model):
    sub_sub_topic_id = models.ForeignKey(CariculamSubTopics, on_delete=models.CASCADE,related_name="c_sub_sub_topic_id_col")
    sub_sub_topic_name = models.CharField(max_length=60,null=True,blank=True)

    class SubSubTopicsProgressStatuses(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         DELAYED  = 'DL',_('Delayed')
         COMPLETED = 'CMP',_('Completed')

    sub_sub_topic_status = models.CharField(max_length=30,choices=SubSubTopicsProgressStatuses.choices,default=SubSubTopicsProgressStatuses.NOT_STARTED,)
    sub_sub_topic_media = models.FileField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_sub_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Topic Sub Subtopics'
        db_table = 'jinoe_cariculam_topic_sub_subtopics'    
    
    def __str__(self):
        return str(self.sub_sub_topic_name)

class CariculamSubSubTopicVideos(models.Model):
    video_sub_sub_topic_id = models.ForeignKey(CariculamSubSubTopic,on_delete=models.CASCADE,related_name="c_video_sub_sub_topic_id_col")
    sub_sub_topic_video_media = models.FileField(max_length=200,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_video_sub_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Topic Sub Subtopic Videos'
        db_table = 'jinoe_cariculam_topic_sub_subtopic_videos'    
    
    def __str__(self):
        return str(self.sub_sub_topic_video_media)

class CariculamSubTopicVideos(models.Model):
    video_sub_topic_id = models.ForeignKey(CariculamSubTopics,on_delete=models.CASCADE,related_name="c_video_sub_topic_id_col")
    sub_topic_video_media = models.FileField(max_length=200,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_video_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Topic Subtopic Videos'
        db_table = 'jinoe_cariculam_topic_subtopic_videos'    
    
    def __str__(self):
        return str(self.sub_topic_video_media)

class CariculamTopicVideos(models.Model):
    video_topic_id = models.ForeignKey(CariculamTopics,on_delete=models.CASCADE,related_name="c_video_topic_id_col")
    topic_video_media = models.FileField(max_length=200,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_topic_video_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Topic Videos'
        db_table = 'jinoe_cariculam_topic_videos'    
    
    def __str__(self):
        return str(self.topic_video_media)



    


