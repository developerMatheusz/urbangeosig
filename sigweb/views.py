from django.shortcuts import render
from sigweb.tasks import query_lote


def map(request):
    return render(request, "sigweb/map.html")


def click_map(request, lng, lat):
    result = query_lote.delay(lng, lat)
    task_result = result.get()
    lote_popup = task_result["lote_popup"] if task_result else None
    lng = task_result["lng"] if task_result else None
    lat = task_result["lat"] if task_result else None

    context = {
        "lote_popup": lote_popup,
        "lng": lng,
        "lat": lat,
    }

    return render(request, "sigweb/click_map.html", context)
