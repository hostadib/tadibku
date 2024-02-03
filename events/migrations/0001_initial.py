# Generated by Django 4.2.1 on 2023-12-16 13:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("location", models.CharField(max_length=255)),
                ("region", models.CharField(max_length=255, null=True)),
                ("title", models.CharField(max_length=255)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                (
                    "cover_event",
                    models.ImageField(blank=True, upload_to="Cover_event/"),
                ),
                ("speaker", models.CharField(max_length=255, null=True)),
                ("speaker_image", models.ImageField(null=True, upload_to="Speaker/")),
                ("speaker_desc", models.CharField(max_length=500, null=True)),
                ("text", ckeditor.fields.RichTextField()),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=0, default=0, max_digits=10, null=True
                    ),
                ),
                ("discount", models.IntegerField(null=True)),
                ("total_slot", models.IntegerField(default=0)),
                ("booked_slot", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.categories",
                    ),
                ),
            ],
        ),
    ]
