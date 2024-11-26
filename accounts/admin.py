from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model. Allows for customized
    display, filtering, permissions, and saving logic specific to the
    accounts application.

    Attributes:
        list_display (tuple): Fields displayed in the admin list view.
        list_filter (tuple): Fields used for filtering in the admin interface.
        search_fields (tuple): Fields available for searching.
        ordering (tuple): Default ordering for the list view.
        list_editable (tuple): Fields editable directly in the list view.
        fieldsets (tuple): Groups of fields displayed on the detail page.
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


# Register the User model with the custom admin configuration
admin.site.register(User, CustomUserAdmin)
