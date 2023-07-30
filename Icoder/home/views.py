from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Contact
from blog.models import Post

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.template import *


def home(request):
    # return HttpResponse("It is a home of Home app")
    # print('Bhavye' in User.objects.values_list('username',flat=True))
    # messages.success(request, 'Your action was successful.')
    return render(request, template_name='home/home.html')


def contact(request):
    # return HttpResponse("It is a contact of Home app")
    if request.method=="POST":
        name = request.POST.get('name','No Name')
        phone = request.POST.get('phone','No phone number')
        email = request.POST.get('email','No email')
        content = request.POST.get('description','No description')
        contactObj = Contact.objects.create(name=name,phone=phone,email=email,content=content)
        contactObj.save()
        return redirect('/')
    return render(request, template_name='home/contact.html')

def about(request):
    return HttpResponse("It is a about of Home app")


def search(request):

    results = []
    query = ""
    if (request.method=="POST"):
        query = request.POST.get("search","no search")
        title = Post.objects.filter(title__icontains=query)
        content = Post.objects.filter(content__icontains=query)
        results = title.union(content)
        
    return render(request,'home/search.html',context={'results':results, 'query':query})
    # return HttpResponse("This is search")

def handleSignUp(request):
    if (request.method=="POST"):
        username = request.POST.get("name",'No name')

        # print(User.objects.all())
        if (username in User.objects.values_list('username',flat=True)):
            return HttpResponse('Username already exists...')
        email = request.POST.get("email",'No email')
        password = request.POST.get("name",'No password')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect("/")
    else:
        return HttpResponse("404 - Not Allowed")

def handleLogin(request):
    if (request.method=="POST"):
        print(request.build_absolute_uri(), type(request.build_absolute_uri), request.get_full_path,type(request.get_full_path))
        email = request.POST.get("Loginemail",'No email')
        password = request.POST.get("Loginpassword",'No password')
        print(email,password)
        # return HttpResponse("Logined")
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            login(request=request, user=user)
            return redirect("/")
    return HttpResponse("404 - Not Allowed")


def handleLogout(request):
    if (request.method=='POST'):
        logout(request)
    # print(request.path)
    return redirect("/")
    