from django.urls import include, path
from .views import StudentListView

app_name = 'schools'

urlpatterns = [
    path("<str:oferta>",StudentListView.as_view(),name="list_students")
]