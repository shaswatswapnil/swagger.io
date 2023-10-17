# Generated by Django 4.2.6 on 2023-10-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GoogleSheetData",
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
                ("Project_Executive", models.CharField(max_length=500)),
                ("Name", models.CharField(max_length=300)),
                ("Handle_Name", models.CharField(max_length=400)),
                ("Password", models.CharField(max_length=100)),
                ("Post_Url", models.CharField(max_length=500)),
                ("Image_Type", models.CharField(max_length=200)),
                ("Video_Type", models.CharField(max_length=200)),
                ("Impressions", models.IntegerField()),
                ("Likes", models.IntegerField()),
                ("Comments", models.IntegerField()),
                ("Retweet", models.IntegerField()),
                ("Followers", models.IntegerField()),
                ("Followings", models.IntegerField()),
            ],
        ),
    ]
