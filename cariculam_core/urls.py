from django.urls import path
from . import views

urlpatterns = [
       path('single-curriculum/<int:pk>',  views.CurriculumDetails.as_view() , name='single_curriculum'),

]