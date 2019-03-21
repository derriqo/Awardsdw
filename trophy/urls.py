from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    url('^$',views.index, name='home'),
    url('^profile/',views.profile,name='profile'),
    url('^project/',views.new_project,name='project'),
    url('^search/',views.search_project,name='search_project'),
    url('^rate/(?P<project_id>[0-9]+)$',views.rating,name='rating')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)