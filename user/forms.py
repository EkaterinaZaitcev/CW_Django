from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import CustomsUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15, required=False, help_text="Необязательное поле. Введите номер телефона"
    )
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomsUser
        fields = ("email", "first_name", "username", "phone_number")
