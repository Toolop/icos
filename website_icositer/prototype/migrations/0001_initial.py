# Generated by Django 3.2.5 on 2021-08-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prototype',
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
                ('nama_anggota3', models.CharField(max_length=100, null=True)),
                ('prodi_anggota3', models.CharField(max_length=100, null=True)),
                ('nama_anggota4', models.CharField(max_length=100, null=True)),
                ('prodi_anggota4', models.CharField(max_length=100, null=True)),
                ('subtema', models.CharField(max_length=100)),
                ('file_abstrak', models.FileField(upload_to='prototype/file_lomba')),
                ('file_ktm', models.FileField(upload_to='prototype/ktm')),
                ('file_foltwib', models.FileField(upload_to='prototype/followtwib')),
            ],
            options={
                'verbose_name_plural': 'Prototype',
                'db_table': 'Prototype',
            },
        ),
    ]
