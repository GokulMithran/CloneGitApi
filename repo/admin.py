from django.contrib import admin

# Register your models here.
from .models import UserProfile,Repository

admin.site.register(UserProfile)
admin.site.register(Repository)