# Generated by Django 4.0.8 on 2023-03-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_alter_application_job_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job_post',
            field=models.CharField(max_length=50),
        ),
    ]
