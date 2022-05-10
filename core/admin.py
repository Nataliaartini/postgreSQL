from django.contrib import admin
from .models import *


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'active', 'modified_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'icon', 'active', 'modified_at')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_role', 'active', 'modified_at')
