# Generated by Django 4.2.1 on 2023-06-16 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0014_rename_category_course_school_category_jur"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="author",
            new_name="author_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="category",
            new_name="category_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="created_at",
            new_name="created_at_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="description",
            new_name="description_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="discount",
            new_name="discount_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="featured_image",
            new_name="featured_image_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="featured_video",
            new_name="featured_video_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="language",
            new_name="language_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="level",
            new_name="level_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="price",
            new_name="price_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="slug",
            new_name="slug_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="status",
            new_name="status_ket",
        ),
        migrations.RenameField(
            model_name="course_keterampilan",
            old_name="title",
            new_name="title_ket",
        ),
    ]