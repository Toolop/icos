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

def virtualex (request):
	return render(request,'virtualexhibition/virtualexhibition.html')

def regist(request):
	return render(request, 'regist.html')