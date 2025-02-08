from django.contrib import admin
from .models import News, Customer, CustomerInfo


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'created_at')
    search_fields = ('user_id',)
    ordering = ('-created_at',)


@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'last_name',
        'first_name',
        'patronymic',
        'phone',
        'email',
        'permission',
        'created_at'
    )
    search_fields = ('last_name', 'first_name', 'customer__user_id', 'email', 'phone')
    list_filter = ('permission', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    list_select_related = ('customer',)
