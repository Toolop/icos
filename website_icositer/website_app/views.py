from django.shortcuts import render

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
	return render(request,'news/news.html')

def detail_news1 (request):
	return render(request,'news/detail_news1.html')

def detail_news2 (request):
	return render(request,'news/detail_news2.html')
