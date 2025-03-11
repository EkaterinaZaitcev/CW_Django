from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from mailing.forms import RecipientForm
from mailing.models import Recipient


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
