"""
Admin Configuration
This module defines custom admin configurations for the User model. It extends
Django's built-in UserAdmin to include additional functionality for managing
user accounts, roles, and approval workflows.

Admin Features:
1. CustomUserAdmin: Provides a tailored admin interface for the User model,
   including:
   - Role and approval status management.
   - Restricted permissions for non-superuser administrators.
   - Field-level and queryset-level customizations.
   - Inline "Change Password" link for users.

Key Features:
- Enhanced user management tailored to application requirements.
- Role-based access control for the admin interface.
- Automated updates to user `is_active` status based on approval workflows.

Dependencies:
- Django's admin framework.
- Models from the accounts app for user management.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.urls import reverse
from django.utils.html import format_html
from .models import User


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model.
    """

    list_display = (
        'username', 'email', 'approval_status', 'is_active', 'role',
        'is_staff'
    )
    list_filter = ('approval_status', 'is_active', 'role')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)
    list_editable = ('approval_status',)

    fieldsets = (
        (None, {
            'fields': (
                'username', 'email', 'role', 'bio', 'experience_level',
                'approval_status', 'is_active', 'profile_completed'
            )
        }),
        ('Permissions', {
            'fields': ('is_staff',),
            'classes': ('collapse',),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        """
        Adjusts fieldsets based on the role of the logged-in user.

        Args:
            request (HttpRequest): The current request object.
            obj (User): The user object being edited (optional).

        Returns:
            tuple: Fieldsets to display in the admin interface.
        """
        fieldsets = super().get_fieldsets(request, obj)
        if (not request.user.is_superuser and request.user.role ==
                User.ADMINISTRATOR):
            fieldsets = (
                (None, {
                    'fields': (
                        'username', 'email', 'role', 'bio',
                        'experience_level', 'approval_status',
                        'is_active', 'profile_completed'
                    )
                }),
            )
        return fieldsets

    def get_queryset(self, request):
        """
        Filters the queryset to exclude superusers and limit visibility to
        captains and crew for administrators.

        Args:
            request (HttpRequest): The current request object.

        Returns:
            QuerySet: The filtered queryset.
        """
        qs = super().get_queryset(request)
        if (not request.user.is_superuser and request.user.role ==
                User.ADMINISTRATOR):
            return qs.filter(
                is_superuser=False, role__in=[User.CAPTAIN, User.CREW]
            )
        return qs

    def has_add_permission(self, request):
        """
        Restricts the ability to add new users to superusers only.

        Args:
            request (HttpRequest): The current request object.

        Returns:
            bool: True if the user is a superuser, otherwise False.
        """
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        """
        Prevents administrators from editing superuser or
        administrator accounts.

        Args:
            request (HttpRequest): The current request object.
            obj (User): The user object being edited (optional).

        Returns:
            bool: True if the user has permission, otherwise False.
        """
        if obj and (obj.is_superuser or obj.role == User.ADMINISTRATOR):
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Prevents deletion of superuser accounts.

        Args:
            request (HttpRequest): The current request object.
            obj (User): The user object being deleted (optional).

        Returns:
            bool: True if the user has permission, otherwise False.
        """
        if obj and obj.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        """
        Automatically updates the `is_active` field
        based on `approval_status`.

        Args:
            request (HttpRequest): The current request object.
            obj (User): The user object being saved.
            form (ModelForm): The form instance with the submitted data.
            change (bool): True if the object is being updated,
            False otherwise.
        """
        if obj.approval_status == User.APPROVED:
            obj.is_active = True
        elif obj.approval_status == User.DISAPPROVED:
            obj.is_active = False
        super().save_model(request, obj, form, change)

    # Add "Change Password" link in the user list
    def password_change_link(self, obj):
        """
        Add a link to change a user's password.
        """
        if obj.pk:
            url = reverse('admin:auth_user_password_change',
                          args=[obj.pk])
            return format_html('<a href="{}">Change Password</a>',
                               url)
        return '-'

    password_change_link.short_description = 'Change Password'

    # Include the password change link in the list_display
    list_display += ('password_change_link',)


# Register the User model with the custom admin configuration
admin.site.register(User, CustomUserAdmin)
