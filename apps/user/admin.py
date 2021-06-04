from django import forms
from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import Group


# Now register the new UserAdmin...

# admin.site.register(UserProfile)
admin.site.unregister(Group)
