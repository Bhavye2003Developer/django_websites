from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "shopHome"),
    path('about/', views.about, name="About Us"),
    path('contact/', views.contact, name="Contact Us"),
    path('thankYou/',views.getContactData, name="contactData"),
    path('tracker/', views.tracker, name="TrackingStatus"),# Staatus
    path('search/', views.search, name="search"),
    path('productView/', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
]
