# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'approval_status', 'is_active', 'role', 'is_staff')
    list_filter = ('approval_status', 'is_active', 'role')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)
    list_editable = ('approval_status',)  # Make `approval_status` editable in the list view

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
            fieldsets = (
                (None, {'fields': ('username', 'email', 'role', 'bio', 'experience_level', 'approval_status', 'is_active', 'profile_completed')}),
            )
        return fieldsets

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser and request.user.role == User.ADMINISTRATOR:
            return qs.filter(is_superuser=False, role__in=[User.CAPTAIN, User.CREW])
        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj and (obj.is_superuser or obj.role == User.ADMINISTRATOR):
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        # Automatically update `is_active` based on `approval_status`
        if obj.approval_status == User.APPROVED:
            obj.is_active = True
        elif obj.approval_status == User.DISAPPROVED:
            obj.is_active = False
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
