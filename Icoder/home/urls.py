from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homehome'),
    path('contact/', views.contact, name='contact'),
    path('about', views.about, name='homeAbout'),
    path('search', views.search, name='search'),
    path('signup',views.handleSignUp, name="handleSignUp"),
    path('login',views.handleLogin, name="handleLoginUp"),
    path('logout',views.handleLogout, name="handleLogout"),
]
