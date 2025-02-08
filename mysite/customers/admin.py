from django.contrib import admin
from .models import CustomerID, CustomerRealInfo, CustomerTelegramInfo, CostumersBillingInfo


@admin.register(CustomerID)
class CustomerIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'created_at')
    search_fields = ('user_id',)
    ordering = ('-created_at',)


@admin.register(CustomerRealInfo)
class CustomerRealInfoAdmin(admin.ModelAdmin):
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


@admin.register(CustomerTelegramInfo)
class CustomerTelegramInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'telegram_username', 'created_at')
    search_fields = ('customer__user_id',)
    ordering = ('-created_at',)
    list_select_related = ('customer',)


@admin.register(CostumersBillingInfo)
class CostumersBillingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'transaction', 'created_at')
    search_fields = ('customer__user_id',)
    ordering = ('-created_at',)
    list_select_related = ('customer',)
