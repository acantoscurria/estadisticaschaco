from django.shortcuts import render
from django.views.generic import ListView
from .models import School
# Create your views here.


class SchoolListView(ListView):
    model= School
    template_name= "schools/list.html"
    context_object_name = 'escuelas'
    