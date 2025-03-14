from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.views import RegisterView

app_name = 'users'

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/',LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='mailing:index'), name='logout'),
]