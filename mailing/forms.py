from django import forms
from django.forms import BooleanField, ModelForm

from mailing.models import Mailing, Message, Recipient


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

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"