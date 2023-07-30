from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("blog/<int:pk>/", views.blog, name="blog-detail"),
    path("create/", views.createBlog, name="blog-create"),
    path("login/", views.loginUser, name="blog-login"),
    path("logout/", views.logoutUser, name="blog-logout"),
    path("register/", views.register, name="blog-register"),
    path("profile/<int:pk>", views.profile, name="blog-profile"),
    path("blogDelete/<int:pk>", views.blogDelete, name="blog-delete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
