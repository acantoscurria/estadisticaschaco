from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    OfferSelectionView,
    OfferSelectionAdminView,
    total_score_chart,
    performance_chart,
    math_ability_chart,
    lan_ability_chart,
    cn_ability_chart,
    cs_ability_chart,
    participation_chart,
    full_participation,
    search_cue
    )

app_name = 'schools'

urlpatterns = [
    path("<int:cue>/offer-selection/",OfferSelectionAdminView.as_view(),name="offer-selection-admin"),
    path("offer-selection/",OfferSelectionView.as_view(),name="offer-selection"),
    path("admin/",TemplateView.as_view(template_name="admin/admin.html"),name="admin"),
    path("<int:cue>/search_cue/",search_cue,name="search_cue"),
    path("performance-chart/<oferta>/",performance_chart,name="performance-chart"),
    path("total-score-chart/<oferta>/",total_score_chart,name="total-score-char"),
    path("math-ability-chart/<oferta>/",math_ability_chart,name="math-ability-chart"),
    path("lan-ability-chart/<oferta>/",lan_ability_chart,name="lan-ability-chart"),
    path("cn-ability-chart/<oferta>/",cn_ability_chart,name="cn-ability-chart"),
    path("cs-ability-chart/<oferta>/",cs_ability_chart,name="cs-ability-chart"),
    path("participation-chart/<oferta>/",participation_chart,name="participation-chart"),
    path("full-participation/<oferta>/",full_participation,name="full-participation"),
]