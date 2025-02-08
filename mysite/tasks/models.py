from django.db import models
from customers.models import CustomerID


class Task(models.Model):
    customer = models.ForeignKey(
        'customers.CustomerID',
        on_delete=models.CASCADE,
        verbose_name='Информация о клиенте',
        related_name='tasks'
    )

    description = models.CharField(max_length=150, verbose_name='Описание задачи')
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('progressing', 'Processing'),
        ('finished', 'Finished '),]

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='waiting',
        verbose_name='Статус задачи'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']
