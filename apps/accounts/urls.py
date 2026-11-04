from django.urls import path

from apps.core.views import planned

app_name = "accounts"

# Implemented in milestone 2 (accounts & onboarding).
urlpatterns = [
    path("login/", planned, {"page": "Log in"}, name="login"),
    path("register/", planned, {"page": "Create your account"}, name="register"),
]
