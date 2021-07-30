from django.db import models

# Create your models here.

class Prototype(models.Model):
	id_pendaftaran		= models.AutoField(primary_key=True)
	nama_ketua			= models.CharField(max_length=100)
	email	  			= models.EmailField(max_length=100)
	no_telepon 			= models.CharField(max_length=100)
	instansi			= models.CharField(max_length=100)
	prodi_ketua			= models.CharField(max_length=100)
	nama_anggota1		= models.CharField(max_length=100, null = True)
	prodi_anggota1		= models.CharField(max_length=100, null = True)
	nama_anggota2		= models.CharField(max_length=100, null = True)
	prodi_anggota2		= models.CharField(max_length=100, null = True)
	subtema				= models.CharField(max_length=100)
	file_pdf			= models.FileField(upload_to='prototype/file_lomba')

	def __str__(self):
		return str(self.nama_ketua)

	class Meta:
		verbose_name_plural = "Prototype"
		db_table = "Prototype"