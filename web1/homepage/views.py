import time
from django.shortcuts import render,redirect,loader
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
import datetime
from django.utils import timezone
from .models import Custom,Event,Attendee
from .forms import CustomCreationForm
from datetime import timedelta
import pytz
import sys

start_time =0
end_time=0

def bookform(request,pk):
    form = Custom.objects.get(id=pk)
    if request.method == 'POST':
        form = Custom.objects.get(id=pk)
        req = request.POST['req']
        start = request.POST['start']
        time = request.POST['time']
        email = request.POST['email']
        starts = start +' '+ time +':' '00'
    
        start_time = datetime.datetime.strptime(starts,"%Y-%m-%d %H:%M:%S")
        end_time  = start_time + timedelta(minutes=45)
        context = { 'req':req,'start':start,'time':time,'start_time':start_time, 'end_time':end_time,'email':email,'form':form}
        return  render(request, 'confirm.html',context)
        

    
    return render(request,'bookform.html',{'form':form})



def confirm(request):
    if request.method == 'POST':
        req = request.POST['required']
        start = request.POST['starts']
        time = request.POST['time']
        email = request.POST['email']
        
        # Sadece veritabanına kaydet
        event = Event.objects.create(
            title=req,
            start_time=start,
            end_time=end_time,
            attendee_email=email
        )
        return redirect('home')
    
    return render(request, 'confirm.html')



def viewevent(request):
    # Şu andan itibarenki etkinlikleri getir
    now = timezone.now()
    events = Event.objects.filter(start_time__gte=now).order_by('start_time')[:10]
    
    event_list = []
    for event in events:
        # Etkinliğin katılımcılarını al
        attendees = list(Attendee.objects.filter(event=event).values_list('email', flat=True))
        
        event_list.append({
            'title': event.title,
            'start': event.start_time,
            'end': event.end_time,
            'attendees': attendees
        })
    
    if not event_list:
        print('No upcoming events found.')
    
    return render(request, 'viewevent.html', {'events': event_list})

def doctor(request):
    form = Custom.objects.filter( )
    
    return render(request,'doctor.html')

def home(request):
    q = request.GET.get('q') 
    # if request.GET.get('q') != None:
    #     blog = Blog.objects.filter(
    #         Q( topic__name__icontains=q) &
    #         Q(draft = False) ) 
        
    # else:
    #     blog = Blog.objects.filter(draft=False)


        
    # topic = Topic.objects.all()
    # drafts = Blog.objects.filter(draft=True)
    
    # context = {'blog':blog,'topics':topic,'list':q,"draft":drafts}
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

