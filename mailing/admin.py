from django.contrib import admin

from mailing.models import MailingAttempt, Recipient, Message


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "full_name", "comments")
    list_filter = ("full_name",)
    search_fields = ("full_name", "email")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "message")
    list_filter = ("title", )
    search_fields = ("title", )

@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "mail_server_response")
    list_filter = ("status",)
    search_fields = ("status",)
