from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Student,StudentForm
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from schools.models import School

# Create your views here.


class StudentListView(LoginRequiredMixin,ListView):
    model = Student
    context_object_name = "estudiantes"
    template_name = "students/list.html"
    login_url = '/'

    def get_queryset(self):
        print(self.request.GET.get("oferta"))
        queryset = Student.objects.filter(service_unit__cueanexo=self.request.user.username).filter(service_unit__oferta 
        = self.kwargs['oferta'])

        self.extra_context={
            "oferta":self.kwargs['oferta'],
            "pk_escuela":queryset[0].service_unit.id
        }

        return queryset

class CreateStudentView(LoginRequiredMixin,CreateView):
    model = Student
    template_name= "students/create.html"
    fields= ["name","last_name","current_cueanexo","to_seccion","to_seccion_type","dni"]

    def form_valid(self, form):
        unit_service = School.objects.get(Q(user=self.request.user) & Q(oferta=self.kwargs["oferta"]))
        form.instance.service_unit = unit_service
        return super().form_valid(form)
   
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""

        self.success_url= reverse("students:list_students",args=[self.kwargs["oferta"]])
        url = self.success_url.format(**self.object.__dict__)

        return url