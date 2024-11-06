# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'approval_status', 'is_active', 'role', 'is_staff')
    list_filter = ('approval_status', 'is_active', 'role')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'role', 'bio', 'experience_level', 'approval_status', 'is_active', 'profile_completed')
        }),
        ('Permissions', {
            'fields': ('is_staff',),
            'classes': ('collapse',),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser and request.user.role == User.ADMINISTRATOR:
            # Show only fields relevant for administrators
            fieldsets = (
                (None, {'fields': ('username', 'email', 'role', 'bio', 'experience_level', 'approval_status', 'is_active', 'profile_completed')}),
            )
        return fieldsets

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Exclude superusers from view for Administrators
        if not request.user.is_superuser and request.user.role == User.ADMINISTRATOR:
            return qs.filter(is_superuser=False, role__in=[User.CAPTAIN, User.CREW])
        return qs

    def has_add_permission(self, request):
        # Prevent Administrator from adding new users
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj:
            # Prevent Administrator from modifying superuser accounts or other administrators
            if obj.is_superuser or obj.role == User.ADMINISTRATOR:
                return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Prevent Administrator from deleting superuser accounts
        if obj and obj.is_superuser and request.user.role == User.ADMINISTRATOR:
            return False
        return super().has_delete_permission(request, obj)

admin.site.register(User, CustomUserAdmin)
