from concurrent.futures.process import _ThreadWakeup
from datetime import datetime, timezone

from re import T
from tabnanny import verbose
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
from django.db import models
from django.contrib.auth.models import User

   
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    about = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin', null=True)

    class Meta:
        verbose_name_plural = 'User profile'
        db_table = 'jinoe_user_profile'
     
    def __str__(self):
        return  str(self.user.first_name)

    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
       UserProfile.objects.create(user=instance)
    instance.userprofile.save()

class Experience(models.Model):
    entery_level_profile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experience_entery_level_profile')
    experience = models.TextField(null = True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exp_created_by', null=True)


    class Meta:
        verbose_name_plural = 'user experience'
        db_table = 'jinoe_user_experience'
     
    def __str__(self):
        return  str(self. entery_level_profile_id.user.username)

    @receiver(post_save, sender=UserProfile)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Experience.objects.create(entery_level_profile_id=instance)


class EducationBacbackground(models.Model):
    entery_level_profile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='education_entery_level_profile')
    education = models.TextField(null = True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ed_created_by', null=True)


    class Meta:
        verbose_name_plural = 'user education'
        db_table = 'jinoe_user_education'
     
    def __str__(self):
        return  str(self. entery_level_profile_id.user.username)

    @receiver(post_save, sender=UserProfile)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            EducationBacbackground.objects.create(entery_level_profile_id=instance)
        



class Certificate(models.Model):
    entery_level_profile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certificate_entery_level_profile')
    certificate = models.TextField(null = True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cer_created_by', null=True)


    class Meta:
        verbose_name_plural = 'user certificate'
        db_table = 'jinoe_user_certificate'
     
    def __str__(self):
        return  str(self. entery_level_profile_id.user.username)

    @receiver(post_save, sender=UserProfile)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Certificate.objects.create(entery_level_profile_id=instance)
     
    

class Skills(models.Model):
    entery_level_profile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills_entery_level_profile')
    skills = models.TextField(null = True)
    create_at = models.DateTimeField(auto_created=True, null = True)
    updated_at = models.DateField(default=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skl_created_by', null=True)


    class Meta:
        verbose_name_plural = 'user skills'
        db_table = 'jinoe_user_skills'
     
    def __str__(self):
        return  str(self. entery_level_profile_id.user.username)

    @receiver(post_save, sender=UserProfile)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Skills.objects.create(entery_level_profile_id=instance)
        
    
