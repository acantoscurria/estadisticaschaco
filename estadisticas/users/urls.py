from django.urls import include, path
from .views import LogoutUserView,CustomLoginView

app_name = 'users'

urlpatterns = [
    path("",CustomLoginView.as_view(),name="custom-login"),
    path("logout/",LogoutUserView.as_view(),name="logout"),
]