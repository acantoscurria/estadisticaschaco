from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from users.models import User
from schools.models import DechDesempenio,DechTotalScore,Participation

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

options_capacidades={
        "Común - Secundaria Completa req. 7 años": {
                                                    "table_name_cn":"dech.capacidad_secundaria_ciencias_naturales",
                                                    "col_name_cn_com": "comunicacion", 
                                                    "col_name_cn_rc": "reconocimiento_de_conceptos", 
                                                    "col_name_cn_as": "analisis_de_situacion", 
                                                    "table_name_cs":"dech.capacidad_secundaria_ciencias_sociales",
                                                    "col_name_cs_as": "analisis_de_situacion", 
                                                    "col_name_cs_if": "interpretacion_de_fuentes", 
                                                    "col_name_cs_rc": "reconocimiento_de_conceptos", 
                                                    "col_name_cs_hyd": "reconocimiento_de_hechos_datos", 
                                                    "table_name_l":"dech.capacidad_secundaria_lengua",
                                                    "col_name_l_rye": "reflexionar_y_evaluar", 
                                                    "col_name_l_int": "interpretar", 
                                                    "col_name_l_ext": "extraer", 
                                                    "table_name_m":"dech.capacidad_secundaria_matematica",
                                                    "col_name_m_rc": "reconocimientos_de_conceptos",
                                                    "col_name_m_com": "comunicacion",
                                                    "col_name_m_rs": "resolucion_de_situacion",
                                                    },
        "Común - Primaria de 7 años": {
                                        "table_name_cn":"dech.capacidad_primaria_ciencias_naturales",
                                        "col_name_cn_com": "comunicacion", 
                                        "col_name_cn_rc": "reconocimiento_de_conceptos", 
                                        "col_name_cn_as": "analisis_de_situacion", 
                                        "table_name_cs":"dech.capacidad_primaria_ciencias_sociales",
                                        "col_name_cs_as": "analisis_de_situacion", 
                                        "col_name_cs_if": "interpretacion_de_fuentes", 
                                        "col_name_cs_rc": "reconocimiento_de_conceptos", 
                                        "col_name_cs_hyd": "reconocimiento_de_hechos_datos", 
                                        "table_name_l":"dech.capacidad_primaria_lengua",
                                        "col_name_l_rye": "reflexionar_y_evaluar", 
                                        "col_name_l_int": "interpretar", 
                                        "col_name_l_ext": "extraer", 
                                        "table_name_m":"dech.capacidad_primaria_matematica",
                                        "col_name_m_rc": "reconocimientos_de_conceptos",
                                        "col_name_m_com": "comunicacion",
                                        "col_name_m_rs": "resolucion_de_situacion",
                                        },
    }
    

colors = [
        'rgba(128, 139, 150,0.7)',
        'rgba(52, 152, 219,0.7)',
        'rgba(72, 201, 176,0.7)',
        'rgba(88, 214, 141  ,0.7)',
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
        return JsonResponse({})
    

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

    data_format = {
            "label": "Puntaje total",
            "data": [],
            "backgroundColor":colors[0],
            }
    try:
        if oferta == "Común - Primaria de 7 años":
            total_score = DechTotalScore.objects.using("detch").raw("select id,pt_m,pt_l,pt_cn,pt_cs from dech.puntaje_primaria where cueanexo = '{}'".format(cueanexo))

            data_format["data"].append(total_score[0].pt_m)
            data_format["data"].append(total_score[0].pt_l)
            data_format["data"].append(total_score[0].pt_cn)
            data_format["data"].append(total_score[0].pt_cs)

        else:
            total_score = DechTotalScore.objects.using("detch").raw("select id,pt_m,pt_l,pt_cn,pt_cs from dech.puntaje_secundaria where cueanexo = '{}'".format(cueanexo))
            data_format["data"].append(total_score[0].pt_m)
            data_format["data"].append(total_score[0].pt_l)
            data_format["data"].append(total_score[0].pt_cn)
            data_format["data"].append(total_score[0].pt_cs)
    except:
        return JsonResponse({})

    datasets.append(data_format)
    
    return JsonResponse(data)

def math_ability_chart(request,oferta):
    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []

    try:
        
        concepto = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_m"),options_capacidades.get(oferta).get("col_name_m_rc")))
        comunicacion = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_m"),options_capacidades.get(oferta).get("col_name_m_com")))
        resolucion = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_m"),options_capacidades.get(oferta).get("col_name_m_rs")))
    except:
        return JsonResponse({})
    

    for i in range(4):
        data_format = {
            "label": "",
            "data": [],
            "backgroundColor": "",
            "stack":"Stack0"
            }
        data_format["label"]=f"Nivel: {concepto[i].desempenio}"
        data_format["data"]=[concepto[i].promedio,comunicacion[i].promedio,resolucion[i].promedio,]
        data_format["backgroundColor"]=colors[i]
        datasets.append(data_format)

    data = {
        "labels": ["Reconocimiento de Conceptos","Comunicación","Resolución de Situación"],
        "datasets": datasets
    }
    return JsonResponse(data)

def lan_ability_chart(request,oferta):
    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []

    try:
        
        reflexion = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_l"),options_capacidades.get(oferta).get("col_name_l_rye")))
        interpretar = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_l"),options_capacidades.get(oferta).get("col_name_l_int")))
        extraer = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_l"),options_capacidades.get(oferta).get("col_name_l_ext")))
    except:
        return JsonResponse({})
    

    for i in range(4):
        data_format = {
            "label": "",
            "data": [],
            "backgroundColor": "",
            "stack":"Stack0"
            }
        data_format["label"]=f"Nivel: {extraer[i].desempenio}"
        data_format["data"]=[extraer[i].promedio,interpretar[i].promedio,reflexion[i].promedio,]
        data_format["backgroundColor"]=colors[i]
        datasets.append(data_format)

    data = {
        "labels": ["Extraer","Interpretar","Reflexión y Evaluación"],
        "datasets": datasets
    }
    return JsonResponse(data)


def cn_ability_chart(request,oferta):
    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []

    try:
        
        conceptos = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cn"),options_capacidades.get(oferta).get("col_name_cn_rc")))
        comunicacion = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cn"),options_capacidades.get(oferta).get("col_name_cn_com")))
        situacion = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cn"),options_capacidades.get(oferta).get("col_name_cn_as")))
    except:
        return JsonResponse({})
    

    for i in range(4):
        data_format = {
            "label": "",
            "data": [],
            "backgroundColor": "",
            "stack":"Stack0"
            }
        data_format["label"]=f"Nivel: {conceptos[i].desempenio}"
        data_format["data"]=[conceptos[i].promedio,comunicacion[i].promedio,situacion[i].promedio,]
        data_format["backgroundColor"]=colors[i]
        datasets.append(data_format)

    data = {
        "labels": ["Reconocimiento de Conceptos","Comunicación","Análisis de Situación"],
        "datasets": datasets
    }
    return JsonResponse(data)

def cs_ability_chart(request,oferta):
    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []

    try:
        
        fuente = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cs"),options_capacidades.get(oferta).get("col_name_cs_if")))
        concepto = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cs"),options_capacidades.get(oferta).get("col_name_cs_rc")))
        situacion = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cs"),options_capacidades.get(oferta).get("col_name_cs_as")))
        hechos = DechDesempenio.objects.using("detch").raw("select * from dech.desempenio('{}','{}','{}')".format(cueanexo,options_capacidades.get(oferta).get("table_name_cs"),options_capacidades.get(oferta).get("col_name_cs_hyd")))
    except:
        return JsonResponse({})
    

    for i in range(4):
        data_format = {
            "label": "",
            "data": [],
            "backgroundColor": "",
            "stack":"Stack0"
            }
        data_format["label"]=f"Nivel: {fuente[i].desempenio}"
        data_format["data"]=[hechos[i].promedio,concepto[i].promedio,fuente[i].promedio,situacion[i].promedio,]
        data_format["backgroundColor"]=colors[i]
        datasets.append(data_format)

    data = {
        "labels": ["Reconocimientos de Hechos / Datos","Reconocimiento de Conceptos","Interpretación de Fuentes","Análisis de Situación"],
        "datasets": datasets
    }
    return JsonResponse(data)


def participation_chart(request,oferta):

    if not oferta:
        return JsonResponse({})
    
    anexo,oferta = oferta.split(" | ")
    cueanexo = request.user.username + anexo
    datasets = []
    nivel=""
    data = {
        "labels": ["Estudiantes presentes","No participaron"],
        "datasets": datasets
    }

    data_format = {
            "label": "Participación",
            "data": [],
            "backgroundColor":[colors[1],colors[0]],
            }
    
    if oferta == "Común - Primaria de 7 años":
        nivel = "primaria"
    else:
        nivel = "secundaria"
    
    participation = Participation.objects.using("detch").raw("select * from dech.participacion_{} where cueanexo = '{}'".format(nivel,cueanexo))
    
    data_format["data"].append(participation[0].porc_participacion)
    data_format["data"].append(participation[0].porc_no_participacion)

    datasets.append(data_format)
    
    return JsonResponse(data)