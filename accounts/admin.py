from django.contrib import admin

from accounts.models import UserProfile,User

admin.site.register(UserProfile)
admin.site.register(User)
