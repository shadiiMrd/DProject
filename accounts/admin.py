from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import *


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('first_name', 'last_name', 'position', 'email', 'phone_number')
    list_filter = ('first_name', 'last_name', 'phone_number')

    fieldsets = (
        ('user', {'fields': ('first_name', 'last_name', 'phone_number', 'position')}),
        ('personal info', {'fields': ('email', 'password')}),
        ('access info', {'fields': ('is_active', 'is_admin',)}),
    )

    add_fieldsets = (
        (None, {'fields': (
            'first_name', 'last_name', 'phone_number', 'password1', 'password2', 'position', 'email', 'is_active',
            'is_admin',)}),
    )

    ordering = ['first_name', 'last_name']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
