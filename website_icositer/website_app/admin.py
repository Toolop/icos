from django.contrib import admin

from website_app.models import News
from prototype.models import Prototype
from poster.models import Poster
from article.models import Article

class ListNews(admin.ModelAdmin):
	list_display = ('judul', 'tanggal',)
	prepopulated_fields = {'slug': ('judul',)}
admin.site.register(News, ListNews)

class ListPrototype(admin.ModelAdmin):
	list_display = ('nama_ketua', 'instansi', 'subtema')
admin.site.register(Prototype, ListPrototype)

class ListPoster(admin.ModelAdmin):
	list_display = ('nama_ketua', 'instansi', 'subtema')
admin.site.register(Poster,ListPoster)

class ListArticle(admin.ModelAdmin):
	list_display = ('nama_ketua', 'instansi', 'subtema')
admin.site.register(Article, ListArticle)