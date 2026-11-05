from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView

from apps.core.views import staff_login

admin.site.site_header = "KKEVO Academy — Content administration"
admin.site.site_title = "KKEVO Academy admin"
admin.site.index_title = "Content management"

urlpatterns = [
    # Staff workspace: one login page, one overview, Unfold-themed admin for data management
    path("admin/login/", staff_login, name="admin_login_redirect"),
    path("admin/logout/", auth_views.LogoutView.as_view(), name="admin_logout_redirect"),
    path("admin/", RedirectView.as_view(pattern_name="studio:overview"), name="admin_home_redirect"),
    path("admin/", admin.site.urls),
    path("studio/", include("apps.studio.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("learn/", include("apps.learning.urls")),
    path("practice/", include("apps.practice.urls")),
    path("", include("apps.courses.urls")),
    path("", include("apps.core.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
