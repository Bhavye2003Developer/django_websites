from django.urls import path
from . import views
urlpatterns = [
    path('<int:userID>',views.home, name='home'),
    path('order/<int:userID>',views.order,name='order'),
    path('gallery/<int:userID>',views.gallery, name='gallery')
]