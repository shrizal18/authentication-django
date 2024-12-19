from django.urls import path

from .views import homepage, signup , log_in, log_out , profile

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup", signup , name="signup"),
    path("login", log_in, name="login"),
    path("logout", log_out, name="logout"),
    path("profile", profile, name="profile")
]