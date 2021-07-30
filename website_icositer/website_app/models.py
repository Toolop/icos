from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
	judul = models.CharField(max_length = 255)
	isi = RichTextField(blank = True, null = True)
	# isi = models.CharField(max_length = 1000)
	tanggal = models.DateField(auto_now_add = True)
	penulis = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return str(self.judul)
	class Meta:
		verbose_name_plural = 'News'
		db_table = "News"