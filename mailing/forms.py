from django import forms
from django.forms import ModelForm

from mailing.models import Recipient


class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient
        fields = '__all__'
        exclude = ['owner']
