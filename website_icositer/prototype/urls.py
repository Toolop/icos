from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
	path('registration', regist, name='regist-pro'),
	path('export-file-xls-prototype', export_prototype_xls, 'export'),
]

app_name = 'prototype'