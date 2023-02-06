from django.urls import include, path
from .views import OfferSelectionView

app_name = 'schools'

urlpatterns = [
    path("offer-selection/",OfferSelectionView.as_view(),name="offer-selection"),
]