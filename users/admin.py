from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomUserCreationForm

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm



admin.site.register(CustomUser, CustomUserAdmin)