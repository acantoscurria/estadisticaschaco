
from django.shortcuts import render,reverse
from django.contrib.auth.views import LogoutView,LoginView
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as auth_login
# Create your views here.
from users.models import User

class LogoutUserView(LogoutView):
    template_name="users/login.html"

class CustomLoginView(UserPassesTestMixin,LoginView):
    template_name= "users/login.html"

    def get_success_url(self):
        return reverse("schools:offer-selection")  # success_url may be lazy
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """

        form = self.get_form()
        try:
            user = User.objects.get(username=request.POST.get("username"))
        except:
            user = None
        if user:
            user.failed_login_attempts += 1
            if user.failed_login_attempts >= 4:
                user.is_active = False
                form.add_error(None, "Has llegado al límite máximo de intentos fallidos, comuníquese con estadísticas educativas")
            user.save()
        if form.is_valid():
            user.failed_login_attempts = 0
            user.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def test_func(self):
        return not self.request.user.is_authenticated