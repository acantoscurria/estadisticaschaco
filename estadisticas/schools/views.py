from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from users.models import User

# Create your views here.


class OfferSelectionView(LoginRequiredMixin,ListView):
    template_name = "schools/offer_charts.html"
    context_object_name = "school_offers"
    login_url = '/'
    
    def get_queryset(self):
        return User.objects.get(username=self.request.user.username).offer_set.values('anexo','oferta')
    


# añadir login required y solo metodo get
def chart_data(request,oferta=None):
    if not oferta:
        return JsonResponse("Es necesario algún valor.")
    
    oferta = oferta.split(" | ")
    print(oferta)
    cue = request.user.username
    
    data = {
        "labels": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
        "datasets": [{
            "label": "Ventas",
            "data": [100, 200, 300, 400, 500],
            "backgroundColor": ["red", "blue", "green", "yellow", "purple"]
        }]
    }


    return JsonResponse(data)