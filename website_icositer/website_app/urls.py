from django.conf.urls import url, include
from django.urls import path
from website_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', homepage, name='home'),
    path('about', about, name='about'),
    path('competition', competition, name='competition'),
    path('conference', conference, name='conference'),
    path('culturalnight', cultnight, name='cultnight'),
    path('virtualexhibition', virtualex, name='virtualex'),
    path('poster', poster, name='poster'),
    path('previus', previus, name='previus'),
    
    path('news', news.as_view(), name='news'),
    path('news/<slug:slug>', detail_news.as_view(), name='detail_news'),

    path('webinar', regiswebinar, name='regiswebinar'),
    path('registration', regisconference, name='regisconference'),
    url(r'^writtenidea/', include('article.urls',namespace='article')),
    url(r'^poster/', include('poster.urls',namespace='poster')),
    url(r'^prototype/', include('prototype.urls',namespace='prototype')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
