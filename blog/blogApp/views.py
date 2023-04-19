from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Blog


def index(request):
    allBlogs = Blog.objects.all()

    return render(request, 'blogApp/home.html', context={'allBlogs':allBlogs})


def detail(request, user_id):

    user = get_object_or_404(Blog, pk = user_id)
    votes = user.votes

    return render(request, "blogApp/particularBlog.html", context={'user':user})


def userBlogs(request, userName):
    allUserBlogs = Blog.objects.filter(author=userName)
    return render(request, 'blogApp/home.html', context={'allBlogs':allUserBlogs})

def increase(request, user_id):
    user = get_object_or_404(Blog, pk = user_id)
    user.votes+=1
    user.save()
    return redirect(to=f"/blog/user/{user.id}")

def decrease(request, user_id):
    user = get_object_or_404(Blog, pk = user_id)
    user.votes-=1
    user.save()
    return redirect(to=f"/blog/user/{user.id}")