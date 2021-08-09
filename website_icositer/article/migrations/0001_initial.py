# Generated by Django 3.2.5 on 2021-08-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_pendaftaran', models.AutoField(primary_key=True, serialize=False)),
                ('nama_ketua', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('no_telepon', models.CharField(max_length=100)),
                ('instansi', models.CharField(max_length=100)),
                ('prodi_ketua', models.CharField(max_length=100)),
                ('nama_anggota1', models.CharField(max_length=100, null=True)),
                ('prodi_anggota1', models.CharField(max_length=100, null=True)),
                ('nama_anggota2', models.CharField(max_length=100, null=True)),
                ('prodi_anggota2', models.CharField(max_length=100, null=True)),
                ('subtema', models.CharField(max_length=100)),
                ('file_abstrak', models.FileField(upload_to='article/file_lomba')),
                ('file_ktm', models.FileField(upload_to='article/ktm')),
                ('file_foltwib', models.FileField(upload_to='article/followtwib')),
            ],
            options={
                'verbose_name_plural': 'Article',
                'db_table': 'Article',
            },
        ),
    ]
