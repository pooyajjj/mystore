from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'phone', 'is_phone_active', 'is_email_active')
    list_filter = ()

    fieldsets = (
        ('Main', {'fields':('email', 'phone', 'first_name', 'last_name', 'password')}),
        ('permissions', {'fields':('is_active', 'last_login', 'is_phone_active', 'is_email_active')}),
    )

    add_fieldsets = (
        (None, {'fields':('username', 'email', 'phone', 'first_name', 'last_name', 'password1', 'password2')}),
    )


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)