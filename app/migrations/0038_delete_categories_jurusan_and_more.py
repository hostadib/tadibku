# Generated by Django 4.2.1 on 2023-07-30 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0037_alter_author_author_profile_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Categories_jurusan",
        ),
        migrations.DeleteModel(
            name="Categories_keterampilan",
        ),
    ]