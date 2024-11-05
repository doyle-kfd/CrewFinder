# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'role', 'is_staff')
    list_filter = ('is_active', 'role')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'bio', 'experience_level', 'profile_completed')}),
    )

    list_editable = ('is_active',)

    def get_queryset(self, request):
        # Allow administrators to view all users, including inactive ones
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.role == User.ADMINISTRATOR:
            return qs
        return qs.filter(is_active=True)  # Default for non-admin users

    def has_change_permission(self, request, obj=None):
        # Allow administrators to edit user profiles
        if request.user.is_superuser or request.user.role == User.ADMINISTRATOR:
            return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        # Allow administrators to add new users
        return request.user.is_superuser or request.user.role == User.ADMINISTRATOR

    def has_delete_permission(self, request, obj=None):
        # Allow administrators to delete users
        return request.user.is_superuser or request.user.role == User.ADMINISTRATOR

admin.site.register(User, CustomUserAdmin)