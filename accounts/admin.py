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
        (None, {'fields': ('role', 'bio', 'experience_level')}),
    )

    list_editable = ('is_active',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Limit Administrators to only seeing Captain and Crew users
        if request.user.role == User.ADMINISTRATOR and not request.user.is_superuser:
            return qs.filter(role__in=[User.CAPTAIN, User.CREW])
        return qs

    def has_change_permission(self, request, obj=None):
        # Allow Administrators to edit only Captain and Crew users
        if request.user.is_superuser:
            return True
        if request.user.role == User.ADMINISTRATOR and obj and obj.role in [User.CAPTAIN, User.CREW]:
            return True
        return False

admin.site.register(User, CustomUserAdmin)
