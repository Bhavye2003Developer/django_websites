from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    events = Event.objects.filter(event_is_featured=True).order_by('event_date')
    upcomming_events = events.filter(event_date__gte=datetime.date.today()).order_by('event_date')
    return render(request, 'events/index.html', {'featured_events': events, 'upcomming_events': upcomming_events})


def event_list(request):
    all_events = Event.objects.all().order_by('event_date')
    return render(request, 'events/event_list.html', {'all_events': all_events})


def create_event(request):
    if request.method == 'POST':
        event_title = request.POST['event_title']
        event_description = request.POST['event_description']
        event_date = request.POST['event_date']
        event_location = request.POST['event_location']
        event_image = request.FILES.get('eventImage', None)
        print(event_image)
        event_is_featured = request.POST['event_is_featured']
        event = Event(event_title=event_title, event_description=event_description, event_date=event_date, event_location=event_location, event_is_featured=event_is_featured, event_image=event_image)
        event.save()
        return redirect('list')
    return render(request, 'events/create_event.html')

def profile(request):
    return render(request, 'events/profile.html')

def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if (password == confirm_password):
            if (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                print('Username or email already exists')
                return redirect('login_user')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login_user')
        else:
            print('Password does not match')

    return render(request, 'events/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('User does not exist')
            return redirect('register')

    return render(request, 'events/login.html')


def logout_user(request):
    logout(request)
    return redirect('login_user')