from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from authentication.models import UserProfile
from core.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class CariculamChatRoom(models.Model):
    chat_room_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='_c_chat_room_user_id_col')
    chat_room_topic_id = models.ForeignKey(Topics,on_delete=models.CASCADE,related_name='_c_chat_room_topic_id_col')    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_chat_room_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Chat Room'
        db_table = 'jinoe_cariculam_chat_room'
     
    def __str__(self):
        return  str(self.chat_room_topic_id)

class CariculamChatRoomMessage(models.Model):
    message_chat_room_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='_c_message_chat_room_user_id_col')
    message_chat_room_id = models.ForeignKey(CariculamChatRoom,on_delete=models.CASCADE,related_name='_c_message_chat_room_id_col')
    message = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)   
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_c_message_chat_room_created_by', null=True)

    class Meta:
        verbose_name_plural = 'Cariculam Chat Room Messages'
        db_table = 'jinoe_cariculam_chat_room_messages'
     
    def __str__(self):
        return  str(self.chat_room_topic_id)