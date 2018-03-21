from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),    
    url(r'^sensor/(?P<pk>\d+)/$', views.sensor_detail, name='sensor_detail'),
    url(r'^sensor/new/$', views.sensor_new, name='sensor_new'),
	url(r'^sensor/(?P<pk>\d+)/edit/$', views.sensor_edit, name='sensor_edit'),
	url(r'^sensor/list/$', views.sensor_list, name='sensor_list'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)