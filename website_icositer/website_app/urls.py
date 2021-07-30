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
    path('virtualex', virtualex, name='virtualex'),
    path('registration', regist, name='regist'),
    url(r'^poster/', include('poster.urls',namespace='poster')),
    url(r'^prototype/', include('prototype.urls',namespace='prototype')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
