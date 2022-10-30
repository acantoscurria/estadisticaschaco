from syslog import LOG_INFO
from django.shortcuts import render
from django.contrib.auth.views import LogoutView,LoginView
# Create your views here.


class LogoutUserView(LogoutView):
    template_name="users/login.html"

class LoginUserView(LoginView):
    template_name= "users/login.html"
    next_page = "/"