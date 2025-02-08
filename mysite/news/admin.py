from django.contrib import admin
from .models import News


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'is_published', 'created_at')
#     search_fields = ('title',)
#     list_filter = ('is_published', 'created_at')
#     ordering = ('-created_at',)
