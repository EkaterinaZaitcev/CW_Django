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

    def __init__(self, args, **kwargs):
        user = kwargs.pop('user', None)
        super.__init__(self, args, **kwargs)
        if user:
            self.fields['recipients'].queryset = Recipient.objects.filter(owner=user)
            self.fields['Message'].queryset = Message.objects.filter(owner=user)
