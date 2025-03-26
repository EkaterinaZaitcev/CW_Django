from django.urls import include, path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (HomeView, MailingAttemptListView, MailingCreateView,
                           MailingDeleteView, MailingDetailsView,
                           MailingListView, MailingUpdateView,
                           MessageCreateView, MessageDeleteView,
                           MessageListView, MessageUpdateView,
                           RecipientCreateView, RecipientDeleteView,
                           RecipientListView)

app_name =MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('recipient/', cache_page(5)(RecipientListView.as_view()), name='recipient_list'),
    path('recipient/create', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient/<int:pk>/delete', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('message/list', cache_page(5)(MessageListView.as_view()), name='message_list'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),
    path('message/<int:pk>/update', MessageUpdateView.as_view(), name='message_update'),
    path('mailing/list', cache_page(5)(MailingListView.as_view()), name='mailing_list'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/<int:pk>/update', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/', MailingDetailsView.as_view(), name='mailing_detail'),
    path('mailingattempt/list', cache_page(5)(MailingAttemptListView.as_view()), name='mailingattempt_list'),
    path('send/', MailingAttemptListView.as_view(), name="send_mail"),
]