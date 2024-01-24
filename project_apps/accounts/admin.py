from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserChangeForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'email', 'is_superuser', 'is_staff')
# Register your models here.


admin.site.register(CustomUser, CustomUserAdmin)