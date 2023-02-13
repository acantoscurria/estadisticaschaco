
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.views import LogoutView,LoginView
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as auth_login
from django.http import JsonResponse

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
    

def info_user(request):
    if request.POST.username:
        try:
            user = User.objects.get(username=request.POST.username)
        except:
            return JsonResponse({'message':"El CUE ingresado no existe o no se encuentra dentro de la base DECH"})
        
        return JsonResponse({"cue":user.username,"nom_est":user.nom_est,})
    

def register(request):

    if request.method == "POST":
            # Obtiene los datos del formulario
            username = request.POST.get("username")
            password = request.POST.get("password")
            password_confirm = request.POST.get("password_confirm")

            if not username:
                return render(
                    request=request,
                    template_name="users/login.html",
                    context={"error_register_form":"Error en registro: El usuario no puede estar vacío."}
                    )

            if password != password_confirm:
                return render(
                    request=request,
                    template_name="users/login.html",
                    context={"error_register_form":"Error en registro: Las contraseñas no coinciden"}
                    )

            user = User.objects.filter(username=username).first()
            if not user:
                return render(
                    request=request,
                    template_name="users/login.html",
                    context={"error_register_form":"Error en registro: El CUE ingresado no existe."}
                    )
            
            if user.password_entered:
                return render(
                    request=request,
                    template_name="users/login.html",
                    context={"error_register_form":"Error en registro: El usuario se encuentra registrado. Si no recuerda la contraseña deberá comunicarse con el Dpto. de estadísticas educativas."}
                    )
            
            user.set_password(password)
            user.set_password = True
            user.save()
            return render(
                request=request,
                template_name="users/login.html",
                context={"message_register_form":"El usuario fue creado exitosamente, ya puedes ingresar."}
                )
            


