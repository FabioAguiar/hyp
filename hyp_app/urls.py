from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),   
	url(r'^peripheral/new/$', views.peripheral_new, name='peripheral_new'),     
	url(r'^peripheral/detail/(?P<pk>\d+)/$', views.peripheral_detail, name='peripheral_detail'),     
	url(r'^peripheral/detail/(?P<pk>\d+)/edit/$', views.peripheral_edit, name='peripheral_edit'),
	
    url(r'^sensor/(?P<pk>\d+)/$', views.sensor_detail, name='sensor_detail'),
    url(r'^sensor/new/$', views.sensor_new, name='sensor_new'),
	url(r'^sensor/(?P<pk>\d+)/edit/$', views.sensor_edit, name='sensor_edit'),
	url(r'^sensor/list/$', views.sensor_list, name='sensor_list'),
	url(r'^actuator/(?P<pk>\d+)/$', views.actuator_detail, name='actuator_detail'),
	url(r'^actuator/new/$', views.actuator_new, name='actuator_new'),
	url(r'^actuator/(?P<pk>\d+)/edit/$', views.actuator_edit, name='actuator_edit'),
	url(r'^actuator/list/$', views.actuator_list, name='actuator_list'),		    
	url(r'^microcontroller/(?P<pk>\d+)/$', views.microcontroller_detail, name='microcontroller_detail'),
	url(r'^microcontroller/new/$', views.microcontroller_new, name='microcontroller_new'),
	url(r'^microcontroller/(?P<pk>\d+)/edit/$', views.microcontroller_edit, name='microcontroller_edit'),
	url(r'^microcontroller/list/$', views.microcontroller_list, name='microcontroller_list'),
	url(r'^control/panel/$', views.control_panel, name='control_panel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)