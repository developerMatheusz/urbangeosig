import random
import geopandas as gpd
from celery import shared_task
from .models import Setor, Quadra, Lote
from django.contrib.gis.geos import GEOSGeometry
from django.db.utils import IntegrityError


@shared_task
def import_data_async(geopackage):
    setor_gdf = gpd.read_file(geopackage, layer="setores")
    quadra_gdf = gpd.read_file(geopackage, layer="quadras")
    lote_gdf = gpd.read_file(geopackage, layer="lotes")
    lote_gdf = lote_gdf.fillna("Não informado!")

    data = []
    for idx, row in setor_gdf.iterrows():
        setor = Setor()
        setor.num_setor = row["setor"]
        setor.geom = GEOSGeometry(f"{row['geometry']}")
        data.append(setor)

    try:
        Setor.objects.bulk_create(data)
    except IntegrityError:
        pass

    data = []
    for idx, row in quadra_gdf.iterrows():
        quadra = Quadra()
        quadra.num_quadra = row["quadra"]
        quadra.geom = GEOSGeometry(f"{row['geometry']}")
        setor = Setor.objects.filter(
            geom__contains=quadra.geom.point_on_surface
        ).first()
        quadra.setor = setor
        data.append(quadra)
    Quadra.objects.bulk_create(data)

    data = []
    for idx, row in lote_gdf.iterrows():
        lote = Lote()
        lote.num_lote = row["lote"]
        lote.geom = GEOSGeometry(f"{row['geometry']}")
        lote.situacao = random.choice(Lote.SITUACAO_CHOICES)[0]
        quadra = Quadra.objects.filter(
            geom__contains=lote.geom.point_on_surface
        ).first()
        lote.quadra = quadra
        data.append(lote)
    Lote.objects.bulk_create(data)
