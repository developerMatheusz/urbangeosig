from django.urls import path
from . import views

app_name = "register"

urlpatterns = [
    path("", views.property_list, name="property_list"),
    path("form_upload/", views.form_upload, name="form_upload"),
    path("import_data/", views.import_data, name="import_data")
]
