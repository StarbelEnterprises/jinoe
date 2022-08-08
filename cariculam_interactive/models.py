from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from cariculam_core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class CariculamQuestions(models.Model):
    topic = models.ForeignKey(CariculamTopics,on_delete=models.CASCADE)
    question = models.TextField(null=True,blank=True)
    points = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)  
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_qn_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Topic Questions'
        db_table = 'jinoe_cariculam_topic_questions'
     
    def __str__(self):
        return  str(self.question)

class CariculamAnswerOptions(models.Model):
    question_id = models.ForeignKey(CariculamQuestions,on_delete=models.CASCADE,related_name='c_answer_options_question')
    answer = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_ans_opt_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Question Answers'
        db_table = 'jinoe_cariculam_question_answers'
     
    def __str__(self):
        return  str(self.answer)

    @receiver(post_save, sender=CariculamQuestions)
    def create_or_update_answer_options(sender, instance, created, **kwargs):
        if created:
            CariculamAnswerOptions.objects.create(question_id=instance)

class CariculamAnswerLogs(models.Model):
    questin_id = models.ForeignKey(CariculamQuestions,on_delete=models.CASCADE)
    answer_log = models.CharField(max_length=60,null=True,blank=True)
    scores = models.IntegerField(default=0)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_ans_log_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Cariculam Answer Logs'
        db_table = 'jinoe_user_cariculam_answer_logs'
     
    def __str__(self):
        return  str(self.answer_log)

class CariculamTopicLikes(models.Model):
    topic_id = models.ForeignKey(CariculamTopics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.BooleanField()
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True) 
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_topic_like_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'User Cariculam Topic Likes'
        db_table = 'jinoe_user_cariculam_topic_likes'
     
    def __str__(self):
        return  str(self.like)

class CariculamTopicRates(models.Model):
    topic_id = models.ForeignKey(CariculamTopics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_created=True, null = True,editable=False)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_topic_rate_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Cariculam Topic Rates'
        db_table = 'jinoe_user_cariculam_topic_rates'
     
    def __str__(self):
        return  str(self.stars)