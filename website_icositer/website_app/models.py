from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

# image = models.ImageField(upload_to='/images', storage=upload_storage) 

class News(models.Model):
	# upload_storage = FileSystemStorage(location='../../DEPLOY', base_url='//files.icositer2021.com/gambar')
	judul = models.CharField(max_length = 255)
	isi = RichTextField(blank = True, null = True)
	gambar = models.ImageField(null=False, blank=False, upload_to="gambar/")
	tanggal = models.DateField(auto_now_add = True)
	is_published = models.BooleanField(default=True)
	slug = models.SlugField(null=True, unique=True)

	def __str__(self):
		return self.judul

	def get_absolute_url(self):
		return reverse('detail_news', kwargs={'slug': self.slug})

	class Meta:
		verbose_name_plural = 'News'
		db_table = "News"