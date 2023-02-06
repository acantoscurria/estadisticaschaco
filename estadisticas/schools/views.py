from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User

# Create your views here.


class OfferSelectionView(LoginRequiredMixin,ListView):
    template_name = "schools/offer_charts.html"
    context_object_name = "school_offers"
    login_url = '/'
    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)