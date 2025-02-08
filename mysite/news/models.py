from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  # Поле не обязательно
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Customer(models.Model):
    user_id = models.CharField(max_length=15, unique=True, verbose_name='Telegram user_id')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'
        ordering = ['-created_at']


class CustomerInfo(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="info"
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
        verbose_name='Роль пользователя'
    )

    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True, null=True)
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name='Почта', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        if self.last_name and self.first_name:
            return f"{self.last_name} {self.first_name}"
        return f"Пользователь {self.customer.user_id}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']
