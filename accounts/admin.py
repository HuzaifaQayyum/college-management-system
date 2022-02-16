from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm, UserUpdateForm

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['full_name', 'email', 'is_active']
    ordering     = ['email']
    add_form     = UserCreationForm
    form         = UserUpdateForm
    model        = get_user_model()

    fieldsets = (
        ('Basic Info',  { 'fields': ('full_name', 'email', 'password')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        ('Basic Info',  { 'fields': ('full_name', 'email', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
