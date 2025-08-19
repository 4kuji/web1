from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('' , views.home , name='home'),
   
    
    path('fundamentals' , views.fundamentals , name='fundamentals'),
    path('billing' , views.billing , name='billing'),
    path('cycles' , views.cycles , name='cycles'),
    path('register/' , views.register , name='register'),
    path('log/' , views.log , name='log'),
    path('logout_form/' , views.logout_form , name='logout_form'),

]