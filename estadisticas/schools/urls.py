from django.urls import include, path
from .views import OfferSelectionView,performance_chart

app_name = 'schools'

urlpatterns = [
    path("offer-selection/",OfferSelectionView.as_view(),name="offer-selection"),
    path("performance-chart/<oferta>",performance_chart,name="performance-chart"),
]