from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'is_active', 'is_superuser']
    list_filter = ['email', 'is_active', 'is_superuser']
    search_fields = ['email']
    ordering = ['email']

    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ("is_superuser", "is_active", "is_staff")}),
        ('Group permissions', {'fields': ("groups", "user_permissions")}),
        ('Important date', {'fields': ("last_login",)}),
    )

    # add user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser"
            )},
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
