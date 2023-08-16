from urbangeosig.celery import app
from django.contrib.gis.geos import GEOSGeometry
from register.models import Lote


@app.task
def query_lote(lng, lat):
    point = GEOSGeometry(f"POINT({lng} {lat})", srid=4326)
    lote = Lote.objects.filter(geom__contains=point).first()

    if lote:
        lote_popup = lote.popup()

        return {
            "lote_popup": lote_popup,
            "lng": lng,
            "lat": lat,
        }
    else:
        return None
