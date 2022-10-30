from django.urls import include, path
from .views import LogoutUserView,LoginUserView

app_name = 'users'

urlpatterns = [
    path("logout/",LogoutUserView.as_view(),name="logout"),
    path("login/",LoginUserView.as_view(),name="login")
]