from django import forms
from django.forms import ModelForm

from mailing.models import Recipient, Message, Mailing


class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient
        fields = '__all__'
        exclude = ['owner']

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['owner']

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'
        exclude = ['owner']
        widgets = {"recipients": forms.CheckboxSelectMultiple(),}
