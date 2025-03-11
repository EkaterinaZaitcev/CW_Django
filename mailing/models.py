from django.db import models

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
