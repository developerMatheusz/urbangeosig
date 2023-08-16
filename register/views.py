from django.shortcuts import render, redirect
from register.tasks import import_data_async


def property_list(request):
    return render(request, "register/property_list.html")


def form_upload(request):
    if request.method == "POST":
        shapefile = request.FILES.get("shapefile")

        if shapefile:
            with open("temp.gpkg", "wb") as f:
                for chunk in shapefile.chunks():
                    f.write(chunk)
            return redirect("register:import_data")

    return render(request, "register/form_upload.html")


def import_data(request):
    geopackage = "temp.gpkg"
    import_data_async.delay(geopackage)

    return redirect("sigweb:map")
