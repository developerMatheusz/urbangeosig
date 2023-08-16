from django.contrib.gis.db import models


class BaseModel(models.Model):
    ativo = models.BooleanField("Ativo", default=True)
    criado = models.DateTimeField("Criado", auto_now=True)
    modificado = models.DateTimeField("Modificado", auto_now=True)

    class Meta:
        abstract = True
