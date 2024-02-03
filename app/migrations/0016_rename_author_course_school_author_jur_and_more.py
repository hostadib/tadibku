# Generated by Django 4.2.1 on 2023-06-17 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0015_rename_author_course_keterampilan_author_ket_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course_school",
            old_name="author",
            new_name="author_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="created_at",
            new_name="created_at_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="description",
            new_name="description_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="discount",
            new_name="discount_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="featured_image",
            new_name="featured_image_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="featured_video",
            new_name="featured_video_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="language",
            new_name="language_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="level",
            new_name="level_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="price",
            new_name="price_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="slug",
            new_name="slug_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="status",
            new_name="status_jur",
        ),
        migrations.RenameField(
            model_name="course_school",
            old_name="title",
            new_name="title_jur",
        ),
    ]