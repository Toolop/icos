from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^regis/$',views.create, name='create'),
	url(r'^$',views.list, name='list'),
	url(r'^export/$', views.export_poster_xls),
]

app_name = 'poster'