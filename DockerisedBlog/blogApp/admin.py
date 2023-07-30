from django.contrib import admin

# Register your models here.
from .models import Blog, UserDatabase

admin.site.register(Blog)
admin.site.register(UserDatabase)