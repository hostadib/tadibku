# Generated by Django 4.2.1 on 2023-06-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0028_remove_video_youtube_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="youtube_id",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
