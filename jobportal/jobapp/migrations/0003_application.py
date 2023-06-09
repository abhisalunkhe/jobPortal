# Generated by Django 4.0.8 on 2023-03-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_cust_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('coverletter', models.TextField()),
            ],
        ),
    ]
