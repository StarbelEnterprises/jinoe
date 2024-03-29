
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

    def get_modules(self):
        return self.module_set.all().order_by('order_by')
    def get_currilum(self):
        return self.subject_set.all()

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

class SubLevelSet(models.Model):
    sub_level_set_level_id = models.ForeignKey(Levels,on_delete=models.CASCADE,related_name="sub_level_set_level_id_col")
    name = models.CharField(max_length=60,null=False,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stlv_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Eduction Sub Level Sets'
        db_table = 'jinoe_sub_level_set'
     
    def __str__(self):
        return  str(self.name)
    
    # @receiver(post_save, sender=Levels)
    # def create_or_update_sub_level_set(sender, instance, created, **kwargs):
    #     if created:
    #         SubLevelSet.objects.create(sub_level_set_level_id=instance)

class SubLevelEntry(models.Model):
    sub_level_entry_set_id = models.ForeignKey(SubLevelSet,on_delete=models.CASCADE,related_name="sub_level_entry_set_id_col")
    name = models.CharField(max_length=60,null=False,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stlv_entry_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Eduction Sub Level Set Elements'
        db_table = 'jinoe_sub_level_set_elements'
     
    def __str__(self):
        return  str(self.name)

    # @receiver(post_save, sender=SubLevelSet)
    # def create_or_update_sub_level_set_entry(sender, instance, created, **kwargs):
    #     if created:
    #         SubLevelEntry.objects.create(sub_level_elem_set_id=instance)
   
class Modules(models.Model):
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
    module_Level_id = models.ForeignKey(Levels, on_delete=models.CASCADE, related_name='module_set',default=0)
    name = models.CharField(max_length= 60, null= True, blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    description = models.TextField(null=True, blank=False)
    order_by = models.IntegerField(null=True, blank=False)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='md_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Level Modules'
        db_table = 'jinoe_level_modules'
     
    def __str__(self):
        print(self.module_type == 'core')
        return  str(self.name)

    @property
    def get_core_offer_module(self):
        return self.module_type == 'core'

class Chapter(models.Model):
    module_chapter_id = models.ForeignKey(Modules, on_delete=models.CASCADE,related_name="module_chapter_id_col",default=0)
    name = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sbj_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Module Chapters'
        db_table = 'jinoe_module_chapters'    
    
    def __str__(self):
        return f'[Module-] {self. module_chapter_id.name}--{self.name}'

class Topics(models.Model):
    topic_chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE,related_name="topic_subject_id_col",default=0)
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
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'Module Topics'
        db_table = 'jinoe_subject_topics'    
    
    def __str__(self):
        return f'{self.topic_chapter_id}--{self.name}'

class SubTopics(models.Model):
    sub_tipic_topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE,related_name="sub_tipic_topic_id_col",default=0)
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
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Subtopics'
        db_table = 'jinoe_topic_subtopics'    
    
    def __str__(self):
        return f'{self.sub_tipic_topic_id.name}-->{self.sub_topic_name}'
    
    @property
    def get_media(self):
        return self.sub_tipic_media.url

class SubSubTopic(models.Model):
    sub_sub_topic_id = models.ForeignKey(SubTopics, on_delete=models.CASCADE,related_name="sub_sub_topic_id_col")
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
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Sub Subtopics'
        db_table = 'jinoe_topic_sub_subtopics'    
    
    def __str__(self):
        return str(self.sub_sub_topic_name)

class SubSubTopicVideos(models.Model):
    video_sub_sub_topic_id = models.ForeignKey(SubSubTopic,on_delete=models.CASCADE,related_name="video_sub_sub_topic_id_col")
    sub_sub_topic_video_media = models.FileField(max_length=200,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_sub_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Sub Subtopic Videos'
        db_table = 'jinoe_topic_sub_subtopic_videos'    
    
    def __str__(self):
        return str(self.sub_sub_topic_video_media)

class SubTopicVideos(models.Model):
    video_sub_topic_id = models.ForeignKey(SubTopics,on_delete=models.CASCADE,related_name="video_sub_topic_id_col")
    sub_topic_video_media = models.FileField(max_length=200,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_sub_topic_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Subtopic Videos'
        db_table = 'jinoe_topic_subtopic_videos'    
    
    def __str__(self):
        return str(self.sub_topic_video_media)

class TopicVideos(models.Model):
    video_topic_id = models.ForeignKey(Topics,on_delete=models.CASCADE,related_name="video_topic_id_col")
    topic_video_media = models.FileField(max_length=200,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_video_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Videos'
        db_table = 'jinoe_topic_videos'    
    
    def __str__(self):
        return str(self.topic_video_media)



    


