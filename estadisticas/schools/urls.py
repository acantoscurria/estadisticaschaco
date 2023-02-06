from django.urls import include, path
from .views import OfferSelectionView,chart_data

app_name = 'schools'

urlpatterns = [
    path("offer-selection/",OfferSelectionView.as_view(),name="offer-selection"),
    path("chart-data/<oferta>",chart_data,name="chart-data"),
]