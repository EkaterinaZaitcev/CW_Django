from django.db import models
from django.utils.timezone import datetime, timedelta

class Recipient(models.Model):
    """Модель получатель рассылки"""
    email = models.EmailField(max_length=255, verbose_name="Письмо", unique=True, help_text="Адрес должен быть уникальным")
    full_name = models.CharField(max_length=50, verbose_name="ФИО")
    comments = models.TextField(verbose_name="Комментарий", blank=True, help_text="")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'
        ordering = ['id',]


class Message(models.Model):
    """Модель сообщения"""
    title = models.CharField(max_length=150, verbose_name="Тема письма")
    message = models.TextField(verbose_name="Тело письма")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['id', ]

class Mailing(models.Model):
    """Рассылка"""
    STATUS_CHOICES = [("завершена", "завершена"), ("создана", "создана"), ("запущена", "запущена")]

    first_send_at = models.DateTimeField(default=datetime.now(), verbose_name="Дата и время первой отправки")
    end_send_at = models.DateTimeField(default=datetime.now() + timedelta(days=1), verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='создана')
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient, verbose_name='Получатели')

    def __str__(self):
        return f'{self.first_send_at}"{self.status}"'

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
        ordering = ("first_send_at", "status")
        permissions = [("can_cancel_mailing", "Can cancel mailing"),]
