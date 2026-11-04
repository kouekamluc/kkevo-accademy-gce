from django.contrib.auth import views as auth_views
from django.urls import path

from . import onboarding, views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # POST only
    path("onboarding/", onboarding.start, name="onboarding"),
    path("onboarding/class/", onboarding.level, name="onboarding_level"),
    path("onboarding/stream/", onboarding.stream, name="onboarding_stream"),
    path("onboarding/subjects/", onboarding.subjects, name="onboarding_subjects"),
    path("onboarding/done/", onboarding.done, name="onboarding_done"),
    path("profile/", views.profile, name="profile"),
    path("profile/password/", views.password_change, name="password_change"),
    path("profile/low-data/", views.toggle_low_data, name="toggle_low_data"),
]
