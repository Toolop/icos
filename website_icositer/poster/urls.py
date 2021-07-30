from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
	path('registration', regist, name='regist'),
	path('export-file-xls-poster', export_poster_xls, 'export'),
]

app_name = 'poster'