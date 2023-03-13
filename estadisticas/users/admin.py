from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    readonly_fields = ('username',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            fieldsets = (
                (None, {
                'fields': ('username', 'password')
                }),
                ('Personal info', 
                 {'fields': ('is_active', 'password_entered', 'failed_login_attempts')}),
            )
        return fieldsets


admin.site.register(User, CustomUserAdmin)





