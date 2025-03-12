from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import RecipientForm, MessageForm, MailingForm
from mailing.models import Recipient, Message, Mailing


class HomeView(TemplateView):
    template_name = 'mailing/index.html'

"""CRUD Получатель рассылки"""
class RecipientListView(ListView):
        model = Recipient

class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    success_message = reverse_lazy('mailing:recipient_list')

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)

class RecipientUpdateView(UpdateView):
    model= Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing:recipient_list')

class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailing:recipient_list')

"""CRUD Сообщения"""
class MessageListView(ListView):
    model = Message

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_message = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

"""CRUD Рассылка"""
class MailingListView(ListView):
    model = Mailing

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_message = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailsView(DetailView):
    model = Mailing

    def get_queryset(self):
        queryset = Mailing.objects.prefetch_related("recipients")
        return queryset
