# Generated by Django 4.2.6 on 2023-10-17 07:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appname", "0003_alter_googlesheetdata_followers_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="googlesheetdata",
            table="Googlesheet",
        ),
    ]