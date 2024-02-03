# Generated by Django 4.2.1 on 2023-06-14 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_level_course_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="what_you_learn",
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
                ("points", models.CharField(max_length=500)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Requirements",
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
                ("points", models.CharField(max_length=500)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
            ],
        ),
    ]
