from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('' , views.home , name='home'),
   
    path('doctor' , views.doctor , name='doctor'), 
    path('viewevent' , views.viewevent , name='viewevent    '),
    path('confirm' , views.confirm , name='confirm'),
    path('bookform/<str:pk>/' , views.bookform , name='bookform'),
    path('register/' , views.register , name='register'),
    path('log/' , views.log , name='log'),
    path('logout_form/' , views.logout_form , name='logout_form'),

]