from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),   
	url(r'^peripheral/new/$', views.peripheral_new, name='peripheral_new'),     
	url(r'^peripheral/detail/(?P<pk>\d+)/$', views.peripheral_detail, name='peripheral_detail'),     
	url(r'^peripheral/detail/(?P<pk>\d+)/edit/$', views.peripheral_edit, name='peripheral_edit'),
	url(r'^peripheral/(?P<pk>\d+)/remove/$', views.peripheral_remove, name='peripheral_remove'),
	url(r'^peripheral/datatable/$', views.peripheral_list, name='peripheral_datatable'),     	
	url(r'^control/panel/$', views.control_panel, name='control_panel'),
	url(r'^weather/station/$', views.weather_station, name='weather_station'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)