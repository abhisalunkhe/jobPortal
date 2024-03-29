# Generated by Django 4.1 on 2024-02-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("job_id", models.IntegerField()),
                ("job_post", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("web", models.CharField(max_length=100)),
                ("link", models.CharField(max_length=80)),
                ("coverletter", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("sub", models.CharField(max_length=30)),
                ("mes", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Emails",
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
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("logo", models.ImageField(upload_to="Company Logo")),
                ("post", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=30)),
                ("job_type", models.CharField(max_length=10)),
                ("date_of_release", models.DateField()),
                ("salary", models.IntegerField()),
                ("job_desc", models.TextField()),
                ("responsibility_desc", models.TextField()),
                ("qualification_desc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Testimonials",
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
                ("profile", models.ImageField(upload_to="Testimonial")),
                ("name", models.CharField(max_length=50)),
                ("profession", models.CharField(max_length=30)),
                ("comment", models.CharField(max_length=50)),
            ],
        ),
    ]
