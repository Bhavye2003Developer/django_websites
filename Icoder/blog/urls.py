from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bloghome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='BlogPost'),
    
    # API to POST a comment
    path('postComment/<str:slug>', views.postComment, name="postComment"),
    
]