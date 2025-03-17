from tkinter.constants import CASCADE

from django.db import models
from django.utils.timezone import datetime, timedelta

from users.models import CustomUser


class Recipient(models.Model):
    """Модель получатель рассылки"""
    email = models.EmailField(max_length=255, verbose_name="Электронный адрес", unique=True, help_text="Адрес должен быть уникальным")
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
    COMPLETED = "completed"
    CREATED = "created"
    RUNNING = "running"
    STATUS_CHOICES = [("завершена", "завершена"), ("создана", "создана"), ("запущена", "запущена")]

    first_send_at = models.DateTimeField(default=datetime.now(), verbose_name="Дата и время первой отправки")
    end_send_at = models.DateTimeField(default=datetime.now() + timedelta(days=1), verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='CREATED', verbose_name="Статус")
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True, related_name="mailing", verbose_name="Сообщение")
    recipients = models.ManyToManyField(Recipient, verbose_name='Получатели', related_name="mailing")


    def __str__(self):
        subject = self.message.title if self.message else "Нет темы"
        recipient_count = self.recipients.count()
        return f"Рассылка № {self.pk}, Тема письма: {subject}, Количество получателей: {recipient_count}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["id",]

class MailingAttempt(models.Model):
    """Модель. Попытка рассылки"""
    SUCCESS = "success"
    FAILURE = "failure"
    STATUS_CHOICES = [("SUCCESS", "Успешно"), ("FAILURE", "Не успешно")]

    attempted_at = models.DateTimeField(verbose_name="Дата и время попытки отправки")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="статус")
    mail_server_response = models.TextField(null=True, blank=True, verbose_name="Ответ сервера")
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="attempts", verbose_name="Рассылка")


    def __str__(self):
        return f"{self.pk} - {self.attempted_at}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
        ordering = ["id", ]
