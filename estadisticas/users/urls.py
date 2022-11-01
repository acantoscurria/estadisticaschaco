from django.urls import include, path
from .views import LogoutUserView,LoginUserView

app_name = 'users'

urlpatterns = [
    path("",LoginUserView.as_view(),name="login"),
    path("logout/",LogoutUserView.as_view(),name="logout"),
]