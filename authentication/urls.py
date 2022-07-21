from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/',  views.Register.as_view() , name='register'),
    path('login/',  views.Login.as_view() , name='login'),
    path('logout/',  views.logout_user , name='logout'),

    #these shoul go to repective app on phase 2
    path('home/',  views.home , name='home'),
    path('modules/',  views.modules , name='modules'),
    path('single-module/',  views.single_module , name='single_module'),
    path('live-discussion/',  views.live_discussion , name='live_discussion'),
    path('carrer-profile', views.carrer_profile, name='carrer_profile'),
    path('forum', views.forum, name='forum'),
    path('webinar', views.webinar, name='webinar')
]