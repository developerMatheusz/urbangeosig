from django.contrib.gis.db import models
from core.models import BaseModel


class Setor(BaseModel):
    num_setor = models.CharField("Número do setor", unique=True, max_length=20)
    geom = models.MultiPolygonField("Geometria", srid=4326)

    def __str__(self):
        return self.num_setor

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"


class Quadra(BaseModel):
    num_quadra = models.CharField("Número da quadra", max_length=20)
    setor = models.ForeignKey("Setor", verbose_name="Setor", on_delete=models.PROTECT)
    geom = models.MultiPolygonField("Geometria", srid=4326)

    def __str__(self):
        return self.num_quadra

    class Meta:
        verbose_name = "Quadra"
        verbose_name_plural = "Quadras"


class Lote(BaseModel):
    SITUACAO_CHOICES = (
        ("a-ser-atendido", "A ser atendido"),
        ("lote-cadastrado", "Lote cadastrado"),
        ("lote-titulado", "Lote titulado"),
    )
    num_lote = models.CharField("Número do lote", max_length=20)
    situacao = models.CharField("Situação", max_length=20, choices=SITUACAO_CHOICES)
    quadra = models.ForeignKey(
        "Quadra", verbose_name="Quadra", on_delete=models.PROTECT
    )
    geom = models.MultiPolygonField("Geometria", srid=4326)

    def __str__(self):
        return self.num_lote

    def popup(self):
        popup = "<ul>"
        popup += f"<li><span>Número do lote:</span> {self.num_lote}</li>"
        popup += f"<li><span>Situação:</span> {self.get_situacao_display()}</li>"
        popup += f"<li><span>Número da quadra:</span> {self.quadra}</li>"
        popup += f"<li><span>Número do setor:</span> {self.quadra.setor}</li>"
        popup += "</ul>"

        return popup

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"
