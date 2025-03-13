from django.urls import path

from user.apps import UserConfig
from user.views import RegisterView

app_name =UserConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),

]