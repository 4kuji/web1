import time
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import render,redirect,loader
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
import datetime
from .models import Custom,Event,Attendee
from .forms import CustomCreationForm
from datetime import timedelta, datetime
import sys



def fundamentals(request):
    if request.method == 'POST':
        req = request.POST['required']
        start = request.POST['starts']
        time_str = request.POST['time']
        email = request.POST['email']
        
        # Zaman string'ini time objesine çevir
        time_obj = datetime.strptime(time_str, "%H:%M").time()
       
        # Seçilen tarih ve saati birleştir
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        start_datetime = datetime.combine(start_date, time_obj)
        
        # Sonraki 1 saat aralığını hesapla
        end_datetime = start_datetime + timedelta(hours=2)
        
        # Aynı tarihte etkinlik var mı kontrol et
        conflicting_events = Event.objects.filter(
            start_time__date=start_date
        )
        
        # Her bir etkinlik için zaman çakışması kontrol et
        for event in conflicting_events:
            # Event zamanını al (zaten time objesi)
            event_time = event.time
            event_start = datetime.combine(event.start_time.date(), event_time)
            event_end = event_start + timedelta(hours=2)
            
            # Zaman çakışması kontrolü
            if (start_datetime < event_end and end_datetime > event_start):
                return render(request, 'not_ available.html')
        
        # Çakışma yoksa veritabanına kaydet
        event = Event.objects.create(
            title=req,
            start_time=start_datetime,
            time=time_obj,
            attendee_email=email
        )
        return redirect('home')
    
    return render(request, 'fundamentals.html')

def billing(request):
    if request.method == 'POST':
        req = request.POST['required']
        start = request.POST['starts']
        time_str = request.POST['time']
        email = request.POST['email']
        
        # Zaman string'ini time objesine çevir
        time_obj = datetime.strptime(time_str, "%H:%M").time()
       
        # Seçilen tarih ve saati birleştir
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        start_datetime = datetime.combine(start_date, time_obj)
        
        # Sonraki 1 saat aralığını hesapla
        end_datetime = start_datetime + timedelta(hours=1)
        
        # Aynı tarihte etkinlik var mı kontrol et
        conflicting_events = Event.objects.filter(
            start_time__date=start_date
        )
        
        # Her bir etkinlik için zaman çakışması kontrol et
        for event in conflicting_events:
            # Event zamanını al (zaten time objesi)
            event_time = event.time
            event_start = datetime.combine(event.start_time.date(), event_time)
            event_end = event_start + timedelta(hours=1)
            
            # Zaman çakışması kontrolü
            if (start_datetime < event_end and end_datetime > event_start):
                return render(request, 'not_ available.html')
        
        # Çakışma yoksa veritabanına kaydet
        event = Event.objects.create(
            title=req,
            start_time=start_datetime,
            time=time_obj,
            attendee_email=email
        )
        return redirect('home')
    
    return render(request, 'billing.html')

def cycles(request):
    if request.method == 'POST':
        req = request.POST['required']
        start = request.POST['starts']
        time_str = request.POST['time']
        email = request.POST['email']
        
        # Zaman string'ini time objesine çevir
        time_obj = datetime.strptime(time_str, "%H:%M").time()
       
        # Seçilen tarih ve saati birleştir
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        start_datetime = datetime.combine(start_date, time_obj)
        
        # Sonraki 1 saat aralığını hesapla
        end_datetime = start_datetime + timedelta(hours=1)
        
        # Aynı tarihte etkinlik var mı kontrol et
        conflicting_events = Event.objects.filter(
            start_time__date=start_date
        )
        
        # Her bir etkinlik için zaman çakışması kontrol et
        for event in conflicting_events:
            # Event zamanını al (zaten time objesi)
            event_time = event.time
            event_start = datetime.combine(event.start_time.date(), event_time)
            event_end = event_start + timedelta(hours=1)
            
            # Zaman çakışması kontrolü
            if (start_datetime < event_end and end_datetime > event_start):
                return render(request, 'not_ available.html')
        
        # Çakışma yoksa veritabanına kaydet
        event = Event.objects.create(
            title=req,
            start_time=start_datetime,
            time=time_obj,
            attendee_email=email
        )
        return redirect('home')
    
    return render(request, 'cycles.html')

def home(request):
    q = request.GET.get('q') 
    return render(request,'home.html')


def register(request):
    form = CustomCreationForm()
    if request.method == "POST":

        form = CustomCreationForm(request.POST, request.FILES)
        if form.is_valid():

            user = form.save(commit  = False)
            user.username = user.username.lower()
            user.save()
            print(user)
            return redirect('log')
  
    return render(request,"register.html",{'form':form})


def log(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Invalid Username or Password')
            return redirect('log')



    else:
        return render(request, 'login.html')
    


def logout_form(request):
    logout(request)
    return redirect('home')

