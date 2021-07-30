from django.db import models

# Create your models here.

class Poster(models.Model):
	nama_ketua			= models.CharField(max_length=100)
	email	  			= models.EmailField(max_length=100)
	no_telepon 			= models.CharField(max_length=100)
	instansi			= models.CharField(max_length=100)
	prodi_ketua			= models.CharField(max_length=100)
	nama_anggota		= models.CharField(max_length=100)
	prodi_anggota		= models.CharField(max_length=100)
	subtema				= models.CharField(max_length=100)

	def __str__(self):
		return str(self.nama_ketua)

	class Meta:
		verbose_name_plural = 'Poster'
		db_table = "Poster"