# Generated by Django 4.2.2 on 2023-07-03 12:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
                ("criado", models.DateTimeField(auto_now=True, verbose_name="Criado")),
                (
                    "modificado",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado"),
                ),
                (
                    "num_setor",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Número do setor"
                    ),
                ),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        srid=4326, verbose_name="Geometria"
                    ),
                ),
            ],
            options={
                "verbose_name": "Setor",
                "verbose_name_plural": "Setores",
            },
        ),
        migrations.CreateModel(
            name="Quadra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
                ("criado", models.DateTimeField(auto_now=True, verbose_name="Criado")),
                (
                    "modificado",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado"),
                ),
                (
                    "num_quadra",
                    models.CharField(max_length=20, verbose_name="Número da quadra"),
                ),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        srid=4326, verbose_name="Geometria"
                    ),
                ),
                (
                    "setor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="register.setor",
                        verbose_name="Setor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Quadra",
                "verbose_name_plural": "Quadras",
            },
        ),
        migrations.CreateModel(
            name="Lote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
                ("criado", models.DateTimeField(auto_now=True, verbose_name="Criado")),
                (
                    "modificado",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado"),
                ),
                (
                    "num_lote",
                    models.CharField(max_length=20, verbose_name="Número do lote"),
                ),
                (
                    "situacao",
                    models.CharField(
                        choices=[
                            ("a-ser-atendido", "A ser atendido"),
                            ("lote-cadastrado", "Lote cadastrado"),
                            ("lote-titulado", "Lote titulado"),
                        ],
                        max_length=20,
                        verbose_name="Situação",
                    ),
                ),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        srid=4326, verbose_name="Geometria"
                    ),
                ),
                (
                    "quadra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="register.quadra",
                        verbose_name="Quadra",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lote",
                "verbose_name_plural": "Lotes",
            },
        ),
    ]
