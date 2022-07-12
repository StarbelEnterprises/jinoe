from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import gettext_lazy as _

class Assessments(models.Model):

    class AssessmentStatus(models.TextChoices):
         SUBJECTS = 'SBJ',_('Subjects')
         TOPICS = 'TPC',_('Topics')
         SUBTOPICS = 'SBTPC',_('SubTopics')
         MODULES  = 'MDL',_('Modules')
         LEVELS = 'LVLS',_('Levels')

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=30,choices=AssessmentStatus.choices, default=AssessmentStatus.SUBTOPICS,)
    name = models.CharField(max_length=60,null=True,blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.CharField(max_length=300,null=False,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessm_created_by', null=True)

    class Meta:
              verbose_name_plural = 'Student Assessments'
              db_table = 'jinoe_student_assessments'
     
    def __str__(self):
              return  str(self.category)
   
