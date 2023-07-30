from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, UserDatabase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    context = {"blogs": Blog.objects.all()}
    return render(request, "blogApp/home.html", context)


def blog(request, pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            blog = Blog.objects.get(pk=pk)
            likesUserArray = blog.likesUserArray
            if request.user.id in likesUserArray:
                return redirect("blog-detail", pk=pk)
            else:
                blog.likes += 1
                likesUserArray.append(request.user.id)
                blog.save()
                return redirect("blog-detail", pk=pk)
        else:
            return redirect("blog-login")
    context = {"blog": Blog.objects.get(pk=pk)}
    return render(request, "blogApp/blog.html", context)


def createBlog(request):
    if request.method == "POST":
        user_id = request.user.id
        author = request.user.username
        title = request.POST["title"]
        content = request.POST["content"]
        Blog.objects.create(
            user_id=user_id, title=title, content=content, author=author, likes=0
        )
        return redirect("blog-home")
    else:
        return render(request, "blogApp/create.html")


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("blog-home")
        else:
            return redirect("blog-register")
    return render(request, "blogApp/login.html")


def logoutUser(request):
    logout(request)
    return redirect("blog-home")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        if username == "":
            return HttpResponse("Username cannot be empty")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create_user(
            username=username, password=password, email=email
        ).save()
        UserDatabase.objects.create(
            id=User.objects.get(username=username).id,
            username=username,
            password=password,
            email=email,
        ).save()
        return redirect("blog-login")
    return render(request, "blogApp/register.html")


def profile(request, pk):
    if request.method == "POST":
        user = UserDatabase.objects.get(pk=pk)
        user.userImage = request.FILES["userImage"]
        user.userImage.name = str(user.id) + ".png"
        print(user.userImage)
        user.save()
        print(user.userImage)
        return redirect("blog-profile", pk=pk)
    context = {
        "user": UserDatabase.objects.get(pk=pk),
        "blogs": Blog.objects.filter(user_id=pk),
    }
    return render(request, "blogApp/profile.html", context)


def blogDelete(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect("blog-profile", pk=request.user.id)