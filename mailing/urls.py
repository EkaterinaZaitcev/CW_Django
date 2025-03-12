from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import HomeView, RecipientListView, RecipientCreateView, RecipientDeleteView, MessageListView, \
    MessageCreateView, MessageDeleteView, MessageUpdateView

app_name =MailingConfig.name

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('', RecipientListView.as_view(), name='recipient_list'),
    path('recipient/create', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient/<int:pk>/delete', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('message/list', MessageListView.as_view(), name='message_list'),
    path('message/create', MessageCreateView.as_view(), name='message'),
    path('message/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),
    path('message/<int:pk>/update', MessageUpdateView.as_view(), name='message_update'),
]