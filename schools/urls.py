from django.urls import include, path
from .views import SchoolListView

app_name = 'schools'

urlpatterns = [
    path("",SchoolListView.as_view(),name="list_schools")
]
