from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from django.contrib import messages

def index(request):
    return redirect("/blog")

def about(request):
    return HttpResponse("This is aboutus page")

def contact(request):
    return HttpResponse("This is contact page")

def Usersignup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User(username = username, email = email, password = password)
    user.save()

    return redirect("/blog")


def Userlogin(request):

    if (request.user.is_authenticated):
        logout(request)

    else:

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            # print("Username doesn't exists")
            messages.error(request, "Username doesn't exists")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print("username or password is incorrect")

    return redirect("/blog")