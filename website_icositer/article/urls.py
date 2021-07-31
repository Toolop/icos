from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
	path('registration', regist, name='regist'),
	path('export-file-xls-article', export_article_xls, 'export'),
]

app_name = 'article'