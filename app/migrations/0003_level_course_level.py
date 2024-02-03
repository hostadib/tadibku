# Generated by Django 4.2.1 on 2023-06-08 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_author_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Level",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="level",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.level"
            ),
        ),
    ]
