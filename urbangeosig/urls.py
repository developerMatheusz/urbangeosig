from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("map/", include("sigweb.urls")),
    path("account/", include("account.urls")),
    path("register/", include("register.urls")),
    path("admin/", admin.site.urls),
]
