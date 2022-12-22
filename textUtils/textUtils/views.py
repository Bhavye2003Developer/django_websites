# I have created this file via touch views.py

from django.http import HttpResponse
from django.shortcuts import render

def home(request): #Home page
    # return HttpResponse ("<h1>This is home page</h1>")
    return render(request=request,template_name='index.html')

def about(request): #About page
    return HttpResponse ("<h1>This is about page</h1>")
    # params = {'name' : 'Bhavye', 'planet' : 'Mars'}
    # return render(request=request,template_name='index.html')

def rmpunction(text):
    punctuations = '''. , ; ( ) { } [ ] " " ' ' ! - / : @ - * ... < > ?'''.split(" ")
    text = list(text)
    text2 = ""
    for i in text:
        if i not in punctuations:
            text2+=i
    # print(text2)
    return text2

def analyse(request): #Analyse page
    text = request.GET.get('string','default')
    text = str(text)
    # print(text)
    # print(list(text))

    rm_on_off = request.GET.get('removepunc','off')
    # print(rm_on_off)
    if (rm_on_off=='on'):
        text = rmpunction(text=text)
    else:
        text = text
    # print(text)
    num_char = -1
    if (request.GET.get('first_capital','off')=='on'):
        text = text.capitalize()
    if (request.GET.get('upper','off')=='on'):
        text = text.upper()
    if (request.GET.get('lower','off')=='on'):
        text = text.lower()
    if (request.GET.get('num_char','off')=='on'):
        num_char = 0
        for i in text:
            if i!=' ':
                num_char+=1
    if (num_char==-1):
        params = {'text':text,'num_char':'Option not selected!'}
    else:
        params = {'text':text,'num_char':num_char}
    # return HttpResponse ("<h1> capitalise letter </h1><br>")
    return render(request,'analyse.html',params)