from django.shortcuts import render, HttpResponse

from shop.models import Product, ContactDetails

from datetime import datetime


# Create your views here.
def index(request):
    all_entries = Product.objects.all()
    params = {'data' : all_entries}
    # for i in all_entries:
    #     print(i.image)
    return render(request,'shop/html/index.html', params)

def about(request):
    # return HttpResponse("About")
    return render(request,'shop/html/about.html')

def contact(request):
    return render(request, 'shop/html/contactUs.html')


def getContactData(request):
    userName = request.POST.get('userName','UserName missing...')
    userEmail = request.POST.get('userEmail','userEmail missing...')
    UserQuery = request.POST.get('UserQuery','Query missing')
    date = datetime.now().date()

    customer = ContactDetails.objects.create(customer_name=userName, customer_email=userEmail,customer_query=UserQuery,query_date=date)

    customer.save()

    return render(request,'shop/html/thankYour.html')


def tracker(request):
    return HttpResponse("Track")

def search(request):
    return HttpResponse("Search")

def productView(request):
    return HttpResponse("productView")

def checkout(request):
    return HttpResponse("Checkout")