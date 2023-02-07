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
                                                    "table_name_cn":"dech.desempenio_secundaria_ciencias_naturales",
                                                    "des_name_cn":"Desempeño Secundaria Ciencias Naturales",
                                                    "col_name_cn": "secundaria_desempenio_cn", 
                                                    "table_name_cs":"dech.desempenio_secundaria_ciencias_sociales",
                                                    "des_name_cs":"Desempeño Secundaria Ciencias Sociales",
                                                    "col_name_cs": "secundaria_desempenio_cs", 
                                                    "table_name_l":"dech.desempenio_secundaria_lengua",
                                                    "des_name_l":"Desempeño Secundaria Ciencias Lengua",
                                                    "col_name_l": "secundaria_desempenio_l", 
                                                    "table_name_m":"dech.desempenio_secundaria_matematica",
                                                    "des_name_m":"Desempeño Secundaria Ciencias Naturales",
                                                    "col_name_m": "secundaria_desempenio_m",
                                                    },
        "Común - Primaria de 7 años ": {
                                                    "table_name_cn":"dech.desempenio_secundaria_ciencias_naturales",
                                                    "des_name_cn":"Desempeño Secundaria Ciencias Naturales",
                                                    "col_name_cn": "secundaria_desempenio_cn", 
                                                    "table_name_cs":"dech.desempenio_secundaria_ciencias_sociales",
                                                    "des_name_cs":"Desempeño Secundaria Ciencias Sociales",
                                                    "col_name_cs": "secundaria_desempenio_cs", 
                                                    "table_name_l":"dech.desempenio_secundaria_lengua",
                                                    "des_name_l":"Desempeño Secundaria Ciencias Lengua",
                                                    "col_name_l": "secundaria_desempenio_l", 
                                                    "table_name_m":"dech.desempenio_secundaria_matematica",
                                                    "des_name_m":"Desempeño Secundaria Ciencias Naturales",
                                                    "col_name_m": "secundaria_desempenio_m",
                                                    },
    }
    
    anexo,oferta = oferta.split(" | ")

    cueanexo = request.user.username + anexo

    datasets = []
    # print(cueanexo,anexo,oferta,options_desempenio[oferta])

    desempenio_math = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name_m"),options_desempenio.get(oferta).get("col_name_m")))
    desempenio_lengua = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name_l"),options_desempenio.get(oferta).get("col_name_l")))
    

    for i,d in enumerate(desempenio_math):
        datasets.append(
            {
            "label": f"Nivel: {d.desempenio}",
            "data": [d.promedio],
            "backgroundColor": colors[i],
            "stack":"Stack0"
            },
        )

    for i,d in enumerate(desempenio_lengua):
        datasets.append(
            {
            "label": f"Nivel: {d.desempenio}",
            "data": [d.promedio],
            "backgroundColor": colors[i],
            "stack":"Stack1"
            },
        )

    data = {
        "labels": ["Matemática","Lengua","Ciencias Naturales","Ciencias Sociales"],
        "datasets": datasets
    }
    print(data)
    return JsonResponse(data)