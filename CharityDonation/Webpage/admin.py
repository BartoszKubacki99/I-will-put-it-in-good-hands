from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Institution, Donation


admin.site.register(Donation)
admin.site.register(Category)
admin.site.register(Institution)