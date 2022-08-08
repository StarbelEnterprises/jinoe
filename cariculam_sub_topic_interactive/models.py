from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from cariculam_core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class CariculamSubTopicQuestions(models.Model):
    topic = models.ForeignKey(CariculamSubTopics,on_delete=models.CASCADE)
    question = models.TextField(null=True,blank=True)
    points = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_qn_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam SubTopic Questions'
        db_table = 'jinoe_cariculam_sub_topic_questions'
     
    def __str__(self):
        return  str(self.question)

class CariculamSubTopicAnswerOptions(models.Model):
    question_id = models.ForeignKey(CariculamSubTopicQuestions,on_delete=models.CASCADE,related_name='_c_answer_options_question')
    answer = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_ans_opt_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam SubTopic Question Answers'
        db_table = 'jinoe_cariculam_sub_topic_question_answers'
     
    def __str__(self):
        return  str(self.answer)

    @receiver(post_save, sender=CariculamSubTopicQuestions)
    def create_or_update_answer_options(sender, instance, created, **kwargs):
        if created:
            CariculamSubTopicAnswerOptions.objects.create(question_id=instance)

class CariculamSubTopicAnswerLogs(models.Model):
    questin_id = models.ForeignKey(CariculamSubTopicQuestions,on_delete=models.CASCADE)
    answer_log = models.CharField(max_length=60,null=False,blank=True)
    scores = models.IntegerField(default=0)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_ans_log_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Cariculam SubTopic Answer Logs'
        db_table = 'jinoe_user_cariculam_subtopic_answer_logs'
     
    def __str__(self):
        return  str(self.answer_log)

class CariculamSubTopicLikes(models.Model):
    topic_id = models.ForeignKey(CariculamSubTopics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_sub_topic_like_created_by', null=True)
    
    class Meta:
        verbose_name_plural = 'User Cariculam SubTopic Likes'
        db_table = 'jinoe_user_cariculam_sub_topic_likes'
     
    def __str__(self):
        return  str(self.like)

class CariculamSubTopicRates(models.Model):
    topic_id = models.ForeignKey(CariculamSubTopics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_sub_topic_rate_created_by', null=True)

    class Meta:
        verbose_name_plural = 'User Cariculam SubTopic Rates'
        db_table = 'jinoe_user_cariculam_sub_topic_rates'
     
    def __str__(self):
        return  str(self.stars)
