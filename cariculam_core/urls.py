from django.urls import path
from . import views

urlpatterns = [
       path('curriculum_details/<int:pk>',  views.CurriculumDetails.as_view(), name='curriculum_details'),

]