from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'customer', 'status', 'created_at')
    search_fields = ('description', 'customer__user_id')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)
    list_select_related = ('customer',)
    readonly_fields = ('created_at', 'changed_at')
