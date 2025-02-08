from django.db import models


class CustomerID(models.Model):
    user_id = models.CharField(max_length=15, unique=True, verbose_name='Telegram user_id')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'ID клиента'
        verbose_name_plural = 'ID клиентов'
        ordering = ['-created_at']


class CustomerRealInfo(models.Model):
    customer = models.ForeignKey(
        "CustomerID",
        on_delete=models.CASCADE,
        verbose_name="Информация о клиенте",
        related_name="Real_info"
    )

    PERMISSION_CHOICES = [
        ('admin', 'Admin'),
        ('superuser', 'Superuser'),
        ('user', 'User'),
        ('spam', 'Spam'),
    ]

    permission = models.CharField(
        max_length=15,
        choices=PERMISSION_CHOICES,
        default='user',
        verbose_name='Роль клиента'
    )

    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True, null=True)
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name='Почта', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        if self.last_name and self.first_name:
            return f"{self.last_name} {self.first_name}"
        return f"Клиент {self.customer.user_id}"

    class Meta:
        verbose_name = 'Информация о клиенте'
        verbose_name_plural = 'Информация о клиентах'
        ordering = ['-created_at']


class CustomerTelegramInfo(models.Model):
    customer = models.ForeignKey(
        "CustomerID",
        on_delete=models.CASCADE,
        verbose_name="Клиент в Telegram",
        related_name="Telegram_Info"
    )

    telegram_username = models.CharField(max_length=30, verbose_name='Имя клиента в Telegram', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        if self.telegram_username:
            return self.telegram_username
        return f"Клиент {self.customer.user_id}"

    class Meta:
        verbose_name = 'Информация о клиенте в Telegram'
        verbose_name_plural = 'Информация о клиентах в Telegram'
        ordering = ['-created_at']


class CostumersBillingInfo(models.Model):
    customer = models.ForeignKey(
        "CustomerID",
        on_delete=models.CASCADE,
        verbose_name="Информация о клиенте",
        related_name="Billing_info"
    )

    transaction = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Транзакции', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f"Транзакции клиента {self.customer.user_id}"

    class Meta:
        verbose_name = 'Транзакции клиента'
        verbose_name_plural = 'Транзакции клиентов'
        ordering = ['-created_at']