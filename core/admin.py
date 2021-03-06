from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
# Register your models here.


from .models import (
    User, Employee, Department, Office, AssetType, 
    Asset, AssetHistory,
    )


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        ('None', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Office)
admin.site.register(AssetType)
admin.site.register(Asset)
admin.site.register(AssetHistory)