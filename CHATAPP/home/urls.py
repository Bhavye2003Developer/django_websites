from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:roomName>/<str:user>', views.room, name="room")
]