from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import HomeView

app_name =MailingConfig.name

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
]