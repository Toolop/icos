from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
	judul = models.CharField(max_length = 255)
	isi = RichTextField(blank = True, null = True)
	gambar = models.ImageField(null=False, blank=False)
	# isi = models.CharField(max_length = 1000)
	tanggal = models.DateField(auto_now_add = True)
	is_published = models.BooleanField(default=True)

	def __str__(self):
		return self.judul
	class Meta:
		verbose_name_plural = 'News'
		db_table = "News"