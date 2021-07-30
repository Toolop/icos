from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^regis/$',views.create, name='create'),
	url(r'^$',views.list, name='list'),
	url(r'^export/$', views.export_prototype_xls),
]

app_name = 'prototype'