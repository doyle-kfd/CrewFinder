from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'role', 'is_staff')
    list_filter = ('is_active', 'role')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    # Display relevant fields, excluding permissions
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'role', 'bio', 'experience_level', 'is_active', 'profile_completed')
        }),
        ('Permissions', {
            'fields': ('is_staff',),
            'classes': ('collapse',),
        }),
    )

    # Restrict certain fields based on the user's role
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser and request.user.role == User.ADMINISTRATOR:
            # Remove 'is_staff' from view for Administrators
            fieldsets = (
                (None, {'fields': ('username', 'email', 'role', 'bio', 'experience_level', 'is_active', 'profile_completed')}),
            )
        return fieldsets

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Exclude superusers from Administrator's view
        if not request.user.is_superuser and request.user.role == User.ADMINISTRATOR:
            return qs.filter(is_superuser=False)
        return qs

    def has_add_permission(self, request):
        # Prevent Administrator from adding new users
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Prevent Administrator from modifying superuser accounts or permissions
        if obj and obj.is_superuser and request.user.role == User.ADMINISTRATOR:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Prevent Administrator from deleting superuser accounts
        if obj and obj.is_superuser and request.user.role == User.ADMINISTRATOR:
            return False
        return super().has_delete_permission(request, obj)

admin.site.register(User, CustomUserAdmin)