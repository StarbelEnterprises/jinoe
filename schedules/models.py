from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import gettext_lazy as _

class SubjectSchedules(models.Model):
    try:        

        class ScheduleStatuses(models.TextChoices):
            NOT_STARTED = 'NST',_('Not_Started')
            DELAYED = 'DL',_('Delayed')
            COMPLETED  = 'CMP',_('Completed')
            POSTPONED = 'PS',_('Postponed')

        subject_id = models.ForeignKey(Modules,on_delete=models.CASCADE)
        user_id = models.ForeignKey(User,on_delete=models.CASCADE)
        startTime = models.DateTimeField()
        endTime = models.DateTimeField()
        status = models.CharField(max_length=30,choices=ScheduleStatuses.choices, 
        default=ScheduleStatuses.NOT_STARTED,)
        remarks = models.TextField(null=False,blank=True)
        create_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True) 
        create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sch_created_by', null=True)

        class Meta:
              verbose_name_plural = 'Subject Schedules'
              db_table = 'jinoe_subject_schedules'
     
        def __str__(self):
              return  str(self.startTime)

        def clean(self):
              if self.remarks == '' and self.status == 'COMPLETED':
                  raise ValidationError({'status': _('Remarks must be set if schedule status is COMPLETED')})
    
    except ValidationError as e:
        non_field_errors = e.message_dict[NON_FIELD_ERRORS]
