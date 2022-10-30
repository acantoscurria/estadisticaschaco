from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import School
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SchoolListView(LoginRequiredMixin,ListView):
    model = School
    template_name = "schools/list.html"
    context_object_name = 'escuela'
    login_url = '/'

    def get_queryset(self):
        try:
            queryset = self.model.objects.filter(cueanexo=self.request.user.username)
        except queryset.DoesNotExist:
            raise Http404("No se encontró lo que estabas buscando.")

        return queryset
