from django.shortcuts import render, redirect
from .models import BusinessMan
from django.http import HttpResponse

# Create your views here.
def home(request, userID):
    try:
        user = BusinessMan.objects.get(userID = userID)
        works = user.worksByUser.split("\n")
        context = {'username':user.username, 'profession':user.profession, 'userImage':user.userImage, 'address':user.address, 'worksByUser':works, 'userID':user.userID} 
        return render(request, 'card/home.html',context=context)
    except Exception as e:
        print("No user found")
        #Error Page
        # return HttpResponse("No page found")
        return render(request, 'card/home.html',context=context)

def order(request, userID):
    try:
        user = BusinessMan.objects.get(userID = userID)
        context = {'userID':user.userID}
        if (request.method=="POST"):
            party_name = request.POST['party_name']
            description = request.POST['description']
            
            text = f"Party Name : {party_name}\nDescription : {description}"
            url = f"https://wa.me/+918595678068?text={text}"

            return redirect(url)
        return render(request, 'card/order-form.html', context=context)
    
    except Exception as e:
        print("No user found")
        #Error Page
        return HttpResponse("No page found")

def gallery(request, userID):
    try:
        user = BusinessMan.objects.get(userID = userID)
        imageArray = [user.galleryImages1, user.galleryImages2, user.galleryImages3, user.galleryImages4, user.galleryImages5]
        # print(imageArray)

        context = {'username':user.username, 'userID':userID, 'imageArray':imageArray}
        return render(request, 'card/gallery.html',context=context)
    
    except Exception as e:
        print("No user found")
        #Error Page
        return HttpResponse("No page found")