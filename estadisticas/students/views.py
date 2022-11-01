from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin

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
            "oferta":self.kwargs['oferta']
        }

        return queryset