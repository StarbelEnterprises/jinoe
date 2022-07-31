from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import gettext_lazy as _

class WebinerUpdates(models.Model):
    try:
        header = models.CharField(max_length=100,null=False,blank=True)
        message = models.TextField(null=True,blank=True)
        image = models.FileField(null=False,blank=True)
        location = models.CharField(max_length=60,null=False,blank=True)
        event_date = models.DateField(default=datetime.now)
        create_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)
        create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wbn_created_by', null=True)

        class Meta:
              verbose_name_plural = 'Webiner Updated'
              db_table = 'jinoe_webiner_updated'
     
        def __str__(self):
              return  str(self.header)   

        def clean(self):
              if self.header == '' and self.event_date >= datetime.datetime.now():
                  raise ValidationError({'event_date': _('Webiner Header information must be set before save')})

    except ValidationError as e:
        non_field_errors = e.message_dict[NON_FIELD_ERRORS]

class WebinerPioneers(models.Model):        
            pioneers_webiner_id = models.ForeignKey(WebinerUpdates,on_delete=models.CASCADE,related_name='pioneers_webiner_id_col')            
            first_name = models.CharField(max_length=60,null=True,blank=True)
            last_name = models.CharField(max_length=60,null=True,blank=True)
            email = models.CharField(max_length=60,null=True,blank=True)

            class WebinerPioneerStatuses(models.TextChoices):
                    HOSTER = 'HST',_('Hoster')
                    PRESENTER = 'PRS',_('Presenter')
                    COHOST  = 'CH',_('Cohost')

            pioneer_category = models.CharField(max_length=30,choices=WebinerPioneerStatuses.choices,default=WebinerPioneerStatuses.HOSTER,)
            image = models.FileField(null=False,blank=True)
            short_description = models.TextField()
            create_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateField(auto_now=True)
            create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wbn_pnr_created_by', null=True)
            
            class Meta:
              verbose_name_plural = 'Webiner Pioneers'
              db_table = 'jinoe_webiner_pioneers'
     
            def __str__(self):
              return  str(self.first_name)

            @receiver(post_save, sender=WebinerUpdates)
            def create_or_update_webiner_pioneers(sender, instance, created, **kwargs):
               if created:
                   WebinerPioneers.objects.create(pioneers_webiner_id=instance)