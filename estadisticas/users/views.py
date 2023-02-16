
from django.shortcuts import render,redirect
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import RedirectView

# Create your views here.
from users.models import User

class LogoutUserView(LogoutView):
    template_name="users/login.html"

class CustomLoginView(LoginView):
    template_name= "users/login.html"

    def get_success_url(self):
        return reverse_lazy("schools:offer-selection")  # success_url may be lazy
    
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
                form.add_error(None, "Has llegado al límite máximo de intentos fallidos, comuníquese con el Dpto. Evaluación Educativa.")
            user.save()
        if form.is_valid():
            user.failed_login_attempts = 0
            user.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
  
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)
    

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
                    context={"error_register_form":"Error en registro: El usuario se encuentra registrado. Si no recuerda la contraseña deberá comunicarse con el Dpto. de Evaluación Educativa."}
                    )
            
            user.set_password(password)
            user.password_entered = True
            user.save()
            return render(
                request=request,
                template_name="users/login.html",
                context={"message_register_form":"El usuario fue creado exitosamente, ya puedes ingresar."}
                )
            


