from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from blog.models import Post, Comment
from django.contrib.auth.admin import User

def Bloghome(request):
    # return HttpResponse("It is a home of blog app")
    allPosts = Post.objects.all()
    return render(request, template_name='blog/blogHome.html',context={'allPosts':allPosts})

def blogPost(request, slug):
    post = Post.objects.filter(sno=slug)
    # print(post)

    comments = Comment.objects.filter(postID=slug)
    # print(comments)

    return render(request, template_name='blog/blogPost.html',context={'post':post, 'comments':comments, 'UserID':slug})
    # return HttpResponse("It is a BlogPost of blog app")

def postComment(request, slug):
    if (request.method=='POST'):
        if request.user.is_authenticated:
            # print(request.user.id, request.user.username)
            post = Post.objects.get(sno=slug)
            comment = Comment.objects.create(postID=post, postComment=request.POST.get('UserComment','No comment'),name=request.user.username)
            comment.save()
            return redirect(f'/blog/{slug}')
        else:
            return HttpResponse("Please login first")
        pass
    return redirect(f"/blog/{slug}")