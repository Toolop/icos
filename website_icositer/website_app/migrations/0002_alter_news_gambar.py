# Generated by Django 3.2.5 on 2021-08-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='gambar',
            field=models.ImageField(upload_to='../../../gambar/'),
        ),
    ]
