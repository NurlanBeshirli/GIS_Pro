from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class Userfield(UserAdmin):
    fieldsets = (
    (None, {'fields': ('name','surname','username','email','user_img','phone','password')}),
)
    
admin.site.register(User, Userfield)
