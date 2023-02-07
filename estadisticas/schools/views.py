from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from users.models import User
from schools.models import DechDesempenio

# Create your views here.


colors = [
        'rgba(49, 66, 175)',
        'rgba(49, 175, 116)',
        'rgba(175, 123, 49)',
        'rgba(131, 69, 119 )',
        ]

class OfferSelectionView(LoginRequiredMixin,ListView):
    template_name = "schools/offer_charts.html"
    context_object_name = "school_offers"
    login_url = '/'
    
    def get_queryset(self):
        return User.objects.get(username=self.request.user.username).offer_set.values('anexo','oferta')
    


# añadir login required y solo metodo get
def chart_data(request,oferta=None):
    if not oferta:
        return JsonResponse({})
    
    options_desempenio={
        "Común - Secundaria Completa req. 7 años": {
                                                    "table_name":"dech.desempenio_secundaria_ciencias_naturales",
                                                    "des_name":"Desempeño Secundaria Ciencias Naturales",
                                                    "col_name": "secundaria_desempenio_cn"
                                                    },
        "Común - Primaria de 7 años ": "dech.desempenio_primaria_ciencias_naturales",
    }
    
    anexo,oferta = oferta.split(" | ")

    cueanexo = request.user.username + anexo

    datasets = []
    print(cueanexo,anexo,oferta,options_desempenio[oferta])
    desempenio = DechDesempenio.objects.using("detch").raw("select * from dech.promedio_cueanexo('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name"),options_desempenio.get(oferta).get("col_name")))
    

    for i,d in enumerate(desempenio):
        datasets.append(
            {
            "label": f"Nivel: {d.desempenio}",
            "data": [d.promedio],
            "backgroundColor": colors[i],
            "stack":"Stack0"
            },
        )

    data = {
        "labels": [f"Desempeño Matemática",],
        "datasets": datasets
    }
    print(data)
    return JsonResponse(data)