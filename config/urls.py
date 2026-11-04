from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "GCE Learning Academy — Content administration"
admin.site.site_title = "GCE Learning Academy admin"
admin.site.index_title = "Content management"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("learn/", include("apps.learning.urls")),
    path("", include("apps.courses.urls")),
    path("", include("apps.core.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
