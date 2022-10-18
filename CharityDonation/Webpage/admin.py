from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Category, Institution, Donation, CustomUser


admin.site.register(Donation)
admin.site.register(Category)
admin.site.register(Institution)

@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)