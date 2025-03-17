from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import HomeView, RecipientListView, RecipientCreateView, RecipientDeleteView, MessageListView, \
    MessageCreateView, MessageDeleteView, MessageUpdateView, MailingListView, MailingCreateView, MailingDeleteView, \
    MailingUpdateView, MailingAttemptListView

app_name =MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('recipient/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient/create', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient/<int:pk>/delete', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('message/list', MessageListView.as_view(), name='message_list'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),
    path('message/<int:pk>/update', MessageUpdateView.as_view(), name='message_update'),
    path('mailing/list', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_form'),
    path('mailing/<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/<int:pk>/update', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_attempt/list', MailingAttemptListView.as_view(), name='mailing_attempt_list'),
]