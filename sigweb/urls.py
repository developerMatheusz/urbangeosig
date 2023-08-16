from django.urls import path
from . import views

app_name = "sigweb"

urlpatterns = [
    path("", views.map, name="map"),
    path("click/<path:lng>/<path:lat>/", views.click_map, name="click_map"),
]
