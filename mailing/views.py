from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import RecipientForm, MessageForm, MailingForm
from mailing.models import Recipient, Message, Mailing, MailingAttempt


class HomeView(TemplateView):
    template_name = 'mailing/index.html'

"""CRUD Получатель рассылки"""
class RecipientListView(LoginRequiredMixin, ListView):
        model = Recipient

class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    success_message = reverse_lazy('mailing:recipient_list')

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)

class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model= Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing:recipient_list')

class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailing:recipient_list')

"""CRUD Сообщения"""
class MessageListView(ListView):
    model = Message

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_message = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

"""CRUD Рассылка"""
class MailingListView(ListView):
    model = Mailing

class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailing/mailing_form.html"
    success_message = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        instance = form.save()
        user = self.request.user
        instance.owner = user
        instance.save()
        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailsView(LoginRequiredMixin, DetailView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

    def get_queryset(self):
        queryset = Mailing.objects.prefetch_related("recipients")
        return queryset

class MailingAttemptCreateView(LoginRequiredMixin, CreateView):
    model = MailingAttempt
    success_url = reverse_lazy('mailing:mailingattempt_list')

    def form_valid(self, form):
        recipient = form.save()
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().get_queryset()
        elif self.request.user.groups.filter(name="Пользователи").exists():
            return super().get_queryset().filter(owner=self.request.user)
        raise PermissionDenied

