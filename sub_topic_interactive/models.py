from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class SubTopicQuestions(models.Model):
    topic = models.ForeignKey(SubTopics,on_delete=models.CASCADE)
    question = models.TextField(null=True,blank=True)
    points = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_qn_created_by', null=True)

    class Meta:
        verbose_name_plural = 'SubTopic Questions'
        db_table = 'jinoe_sub_topic_questions'
     
    def __str__(self):
        return  str(self.question)

class SubTopicAnswerOptions(models.Model):
    question_id = models.ForeignKey(SubTopicQuestions,on_delete=models.CASCADE,related_name='answer_options_question')
    answer = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_ans_opt_created_by', null=True)

    class Meta:
        verbose_name_plural = 'SubTopic Question Answers'
        db_table = 'jinoe_sub_topic_question_answers'
     
    def __str__(self):
        return  str(self.answer)

    @receiver(post_save, sender=SubTopicQuestions)
    def create_or_update_answer_options(sender, instance, created, **kwargs):
        if created:
            SubTopicAnswerOptions.objects.create(question_id=instance)

class SubTopicAnswerLogs(models.Model):
    questin_id = models.ForeignKey(SubTopicQuestions,on_delete=models.CASCADE)
    answer_log = models.CharField(max_length=60,null=True,blank=True)
    scores = models.IntegerField(default=0)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_ans_log_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User SubTopic Answer Logs'
        db_table = 'jinoe_user_sub_topic_answer_logs'
     
    def __str__(self):
        return  str(self.answer_log)

class SubTopicLikes(models.Model):
    topic_id = models.ForeignKey(SubTopics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.BooleanField()
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_topic_like_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'User SubTopic Likes'
        db_table = 'jinoe_user_sub_topic_likes'
     
    def __str__(self):
        return  str(self.like)

class SubTopicRates(models.Model):
    topic_id = models.ForeignKey(SubTopics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_topic_rate_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User SubTopic Rates'
        db_table = 'jinoe_user_sub_topic_rates'
     
    def __str__(self):
        return  str(self.stars)
