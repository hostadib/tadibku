# Generated by Django 4.2.1 on 2023-12-13 06:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0043_usercourseprogress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="about_author",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]