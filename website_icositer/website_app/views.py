from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import News
# Create your views here.
def homepage (request):
	return render(request,'home/home.html')

def about (request):
	return render(request,'about/about.html')

def competition (request):
	return render(request,'competition/competition.html')

def conference (request):
	return render(request,'conference/conference.html')

def cultnight (request):
	return render(request,'cultnight/cultnight.html')

def virtualex (request):
	return render(request,'virtualexhibition/virtualexhibition.html')

def poster (request):
	return render(request,'conference/poster.html')

def previus (request):
	return render(request,'conference/previus.html')

def regisconference (request):
	return render(request,'conference/regis.html')

def news (request):
	berita_utama = News.objects.last()
	berita = News.objects.filter(is_published=True).order_by('-id')[1:4]
	context ={
	'berita_utama':berita_utama,
	'berita':berita,
	}
	return render(request,'news/news.html', context)

def detail_news (request):
	berita_utama = News.objects.last()
	berita = News.objects.filter(is_published=True).order_by('-id')[1:4]
	context ={
	'berita_utama':berita_utama,
	'berita':berita,
	}
	return render(request,'news/detail_news.html',context)
