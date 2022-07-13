from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import gettext_lazy as _

class PerformanceObjectives(models.Model):

    class ObjectiveStatus(models.TextChoices):
         NOT_STARTED = 'NST',_('Not_Started')
         STARTED = 'ST',_('Started')
         AGREED  = 'AGR',_('Agreed')
         DISAGREED = 'DSAG',_('Disagreed')

    class EvaluationStatus(models.TextChoices):
        ASSESSED = 'ASD', _('Assessed')
        UNASSESSED = 'UASD', _('Unassessed')

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    objective = models.TextField(null=True,blank=True)
    required_resources = models.BooleanField()
    duration = models.CharField(max_length=60,null=False,blank=True)
    objective_score = models.IntegerField(default=0)
    objective_status = models.CharField(max_length=30,choices=ObjectiveStatus.choices,
        default=ObjectiveStatus.NOT_STARTED,)
    evaluation_status = models.CharField(max_length=30,choices=EvaluationStatus.choices,
        default=EvaluationStatus.UNASSESSED,)
    objective_goals = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pm_obj_created_by', null=True)

    class Meta:
              verbose_name_plural = 'Performance Objectives'
              db_table = 'jinoe_performance_objectives'
     
    def __str__(self):
              return  str(self.startTime)

class PerformanceEvaluation(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    test_standards = models.TextField(null=False,blank=True)
    remarks = models.TextField(null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pm_evls_created_by', null=True)

    class Meta:
              verbose_name_plural = 'Performance Evaluations'
              db_table = 'jinoe_performance_evaluations'
     
    def __str__(self):
              return  str(self.startTime)

class ReputationQuality(models.Model):
    reputation_quality_evaluation_id = models.ForeignKey(PerformanceEvaluation,on_delete=models.CASCADE)
    reputation_quality = models.TextField(null=False,blank=True)
    student_score = models.IntegerField(default=0)
    supervisor_score = models.IntegerField(default=0)
    agreed_score = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pm_rp_qlt_created_by', null=True)

    class Meta:
              verbose_name_plural = 'Performance Reputation Quality'
              db_table = 'jinoe_performance_reputation_quality'
     
    def __str__(self):
              return  str(self.startTime)

    @receiver(post_save, sender=PerformanceEvaluation)
    def create_or_update_evaluation_reputations(sender, instance, created, **kwargs):
        if created:
            ReputationQuality.objects.create(reputation_quality_evaluation_id=instance)

class ObjectiveResources(models.Model):
    resources_objective_id = models.ForeignKey(PerformanceObjectives,on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pm_obj_resrc_created_by', null=True)

    class Meta:
              verbose_name_plural = 'Performance Objective Resources'
              db_table = 'jinoe_performance_objective_resources'
     
    def __str__(self):
              return  str(self.startTime)
    
    @receiver(post_save,sender=PerformanceObjectives)
    def create_or_update_objective_resources(sender, instance, created, **kwargs):
        if created:
            ObjectiveResources.objects.create(resources_objective_id=instance)











