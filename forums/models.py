from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class Discussion(models.Model):
    discussion_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='discussion_user_id_col')
    header = models.CharField(max_length=300,null=False,blank=True)
    main_body = models.TextField(null=True,blank=True)
    image = models.FileField(null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disc_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Discussions'
        db_table = 'jinoe_discussions'
     
    def __str__(self):
        return  str(self.header)
    
class DiscussionLikes(models.Model):
    likes_discussion_id = models.ForeignKey(Discussion,on_delete=models.CASCADE,related_name='likes_discussion_id_col')
    like = models.BooleanField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disc_likes_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Discussions Likes'
        db_table = 'jinoe_discussions_likes'
     
    def __str__(self):
        return  str(self.like)

class DiscussionReply(models.Model):
    reply_discussion_id = models.ForeignKey(Discussion,on_delete=models.CASCADE,related_name='reply_discussion_id_col')
    reply_discussion_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reply_discussion_user_id_col')
    comment = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disc_reply_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Discussions Replies'
        db_table = 'jinoe_discussions_replies'
     
    def __str__(self):
        return  str(self.like)

    

