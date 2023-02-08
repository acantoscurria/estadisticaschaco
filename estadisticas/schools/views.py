from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from users.models import User
from schools.models import DechDesempenio,DechTotalScore

# Create your views here.
options_desempenio={
        "Común - Secundaria Completa req. 7 años": {
                                                    "table_name_cn":"dech.desempenio_secundaria_ciencias_naturales",
                                                    "des_name_cn":"Desempeño Secundaria Ciencias Naturales",
                                                    "col_name_cn": "secundaria_desempenio_cn", 
                                                    "table_name_cs":"dech.desempenio_secundaria_ciencias_sociales",
                                                    "des_name_cs":"Desempeño Secundaria Ciencias Sociales",
                                                    "col_name_cs": "secundaria_desempenio_cs", 
                                                    "table_name_l":"dech.desempenio_secundaria_lengua",
                                                    "des_name_l":"Desempeño Secundaria Lengua",
                                                    "col_name_l": "secundaria_desempenio_l", 
                                                    "table_name_m":"dech.desempenio_secundaria_matematica",
                                                    "des_name_m":"Desempeño Secundaria Matemática",
                                                    "col_name_m": "secundaria_desempenio_m",
                                                    },
        "Común - Primaria de 7 años": {
                                                    "table_name_cn":"dech.desempenio_primaria_ciencias_naturales",
                                                    "des_name_cn":"Desempeño Primaria Ciencias Naturales",
                                                    "col_name_cn": "primaria_desempenio_cn", 
                                                    "table_name_cs":"dech.desempenio_primaria_ciencias_sociales",
                                                    "des_name_cs":"Desempeño Primaria Ciencias Sociales",
                                                    "col_name_cs": "primaria_desempenio_cs", 
                                                    "table_name_l":"dech.desempenio_primaria_lengua",
                                                    "des_name_l":"Desempeño Primaria Lengua",
                                                    "col_name_l": "primaria_desempenio_l", 
                                                    "table_name_m":"dech.desempenio_primaria_matematica",
                                                    "des_name_m":"Desempeño Primaria Matemática",
                                                    "col_name_m": "primaria_desempenio_m",
                                                    },
    }
    

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
def performance_chart(request,oferta=None):
    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []

    try:
        
        desempenio_math = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name_m"),options_desempenio.get(oferta).get("col_name_m")))
        desempenio_lengua = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name_l"),options_desempenio.get(oferta).get("col_name_l")))
        desempenio_cs = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name_cn"),options_desempenio.get(oferta).get("col_name_cn")))
        desempenio_cn = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_desempenio.get(oferta).get("table_name_cs"),options_desempenio.get(oferta).get("col_name_cs")))
    except:
        return JsonResponse({"ocurrió una excepción"})
    

    for i in range(4):
        data_format = {
            "label": "",
            "data": [],
            "backgroundColor": "",
            "stack":"Stack0"
            }
        data_format["label"]=f"Nivel: {desempenio_math[i].desempenio}"
        data_format["data"]=[desempenio_math[i].promedio,desempenio_lengua[i].promedio,desempenio_cs[i].promedio,desempenio_cn[i].promedio]
        data_format["backgroundColor"]=colors[i]
        datasets.append(data_format)

    data = {
        "labels": ["Matemática","Lengua","Ciencias Naturales","Ciencias Sociales"],
        "datasets": datasets
    }
    return JsonResponse(data)

#ver permisos, al menos de login
def total_score_chart(request,oferta=None):

    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []
    data = {
        "labels": ["Matemática","Lengua","Ciencias Naturales","Ciencias Sociales"],
        "datasets": datasets
    }

    if oferta == "Común - Primaria de 7 años":
        total_score = DechTotalScore.objects.using("detch").raw("select id,pt_m,pt_l,pt_cn,pt_cs from dech.puntaje_primaria where cueanexo = '{}'".format(cueanexo))
        print(total_score.columns)
        data_format = {
            "label": "Puntaje total",
            "data": [],
            "backgroundColor":colors[0],
            }

        data_format["data"].append(total_score[0].pt_m)
        data_format["data"].append(total_score[0].pt_l)
        data_format["data"].append(total_score[0].pt_cn)
        data_format["data"].append(total_score[0].pt_cs)

        datasets.append(data_format)

    else:
        data = {}

    print(data)
    
    return JsonResponse(data)