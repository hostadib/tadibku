# Generated by Django 4.2.1 on 2023-06-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_usercourse_balance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usercourse",
            name="balance",
        ),
    ]
