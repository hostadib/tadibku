# Generated by Django 4.2.1 on 2023-06-26 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0024_rename_course_lesson_course_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lesson",
            old_name="course_id",
            new_name="course",
        ),
    ]
