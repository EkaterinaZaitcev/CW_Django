from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mailing:index")
