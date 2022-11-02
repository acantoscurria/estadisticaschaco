from django.urls import include, path
from .views import StudentListView,CreateStudentView

app_name = 'students'

urlpatterns = [
    path("<str:oferta>",StudentListView.as_view(),name="list_students"),
    path("create/<str:oferta>",CreateStudentView.as_view(),name="create_student")
]