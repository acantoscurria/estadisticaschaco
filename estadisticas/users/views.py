from syslog import LOG_INFO
from django.shortcuts import render,reverse
from django.contrib.auth.views import LogoutView,LoginView
# Create your views here.


class LogoutUserView(LogoutView):
    template_name="users/login.html"

class LoginUserView(LoginView):
    template_name= "users/login.html"

    def get_success_url(self):
        return reverse("schools:list_schools")  # success_url may be lazy