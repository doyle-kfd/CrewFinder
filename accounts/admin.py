# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'role')
    list_filter = ('is_active', 'role', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)  # Order users by date joined (most recent first)

    # Add only custom fields to avoid duplicates
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'bio', 'experience_level')}),
    )

    # Optional: Allow quick edits for user activation
    list_editable = ('is_active',)  # Add this if you'd like quick activation toggling

admin.site.register(User, CustomUserAdmin)
