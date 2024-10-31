from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_approved', 'is_staff', 'role')
    list_filter = ('is_approved', 'role', 'is_staff')
    search_fields = ('username', 'email')

    # Add `is_approved` to the edit view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_approved', 'role')}),
    )

admin.site.register(User, CustomUserAdmin)