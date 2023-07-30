from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is my blog website")
    return render(request, 'blog/index.html')