from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class Questions(models.Model):
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE)
    question = models.TextField(null=True,blank=True)
    points = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)  
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qn_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Topic Questions'
        db_table = 'jinoe_topic_questions'
     
    def __str__(self):
        return  str(self.question)

class AnswerOptions(models.Model):
    question_id = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='answer_options_question')
    answer = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ans_opt_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Question Answers'
        db_table = 'jinoe_question_answers'
     
    def __str__(self):
        return  str(self.answer)

    @receiver(post_save, sender=Questions)
    def create_or_update_answer_options(sender, instance, created, **kwargs):
        if created:
            AnswerOptions.objects.create(question_id=instance)

class AnswerLogs(models.Model):
    questin_id = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer_log = models.CharField(max_length=60,null=True,blank=True)
    scores = models.IntegerField(default=0)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ans_log_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Answer Logs'
        db_table = 'jinoe_user_answer_logs'
     
    def __str__(self):
        return  str(self.answer_log)

class TopicLikes(models.Model):
    topic_id = models.ForeignKey(Topics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.BooleanField()
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True) 
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_like_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'User Topic Likes'
        db_table = 'jinoe_user_topic_likes'
     
    def __str__(self):
        return  str(self.like)

class TopicRates(models.Model):
    topic_id = models.ForeignKey(Topics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_rate_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Topic Rates'
        db_table = 'jinoe_user_topic_rates'
     
    def __str__(self):
        return  str(self.stars)