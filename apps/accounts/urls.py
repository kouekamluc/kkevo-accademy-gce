from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

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
    path("profile/move-up/", views.move_up, name="move_up"),
    path("profile/password/", views.password_change, name="password_change"),
    path("profile/low-data/", views.toggle_low_data, name="toggle_low_data"),
    path("profile/download/", views.data_export, name="data_export"),
    path("profile/delete/", views.delete_account, name="delete_account"),
    path("deleted/", TemplateView.as_view(template_name="accounts/account_deleted.html"), name="account_deleted"),
    path("password-reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/sent/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
