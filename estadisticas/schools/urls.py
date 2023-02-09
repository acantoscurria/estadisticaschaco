from django.urls import include, path

from .views import (
    OfferSelectionView,
    total_score_chart,
    performance_chart,
    math_ability_chart,
    lan_ability_chart,
    cn_ability_chart,
    cs_ability_chart,
    participation_chart
    )

app_name = 'schools'

urlpatterns = [
    path("offer-selection/",OfferSelectionView.as_view(),name="offer-selection"),
    path("performance-chart/<oferta>",performance_chart,name="performance-chart"),
    path("total-score-chart/<oferta>",total_score_chart,name="total-score-char"),
    path("math-ability-chart/<oferta>",math_ability_chart,name="math-ability-chart"),
    path("lan-ability-chart/<oferta>",lan_ability_chart,name="lan-ability-chart"),
    path("cn-ability-chart/<oferta>",cn_ability_chart,name="cn-ability-chart"),
    path("cs-ability-chart/<oferta>",cs_ability_chart,name="cs-ability-chart"),
    path("participation-chart/<oferta>",participation_chart,name="participation-chart"),
]