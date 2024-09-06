from django.contrib import admin
# from blog.models import UserProfile
# # # Register your models here.

# admin.site.register(UserProfile) 

from .models import UserProfile1

admin.site.register(UserProfile1)