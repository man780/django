from django.contrib import admin
from .models import Entity, Property


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ['id', 'modified_by', 'value']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
