from django.urls import path
from . import views

app_name="blogApp"

urlpatterns = [
    path('', views.index, name='home'),
    path('user/<int:user_id>', views.detail, name='detail'),
    path('<str:userName>', views.userBlogs, name="userName"),
    path('increase/<int:user_id>', views.increase, name="increase"),
    path('decrease/<int:user_id>', views.decrease, name="decrease"),
]
