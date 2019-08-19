from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.signIn, name='signIn'),
    #url(r'^dashboard/$',views.postSign, name='postSign'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.logout, name='logout'),
    #url(r'^$', views.dashboard, name='dashboard'),
	url(r'^cycle/new/$', views.cycle_new, name='cycle_new'),
	url(r'^cycle/detail/(?P<pk>\d+)/$', views.cycle_detail, name='cycle_detail'),
	url(r'^cycle/(?P<pk>\d+)/remove/$', views.cycle_remove, name='cycle_remove'),
	url(r'^cycle/datatable/$', views.cycle_list, name='cycle_datatable'),
	url(r'^peripheral/new/$', views.peripheral_new, name='peripheral_new'),
	url(r'^peripheral/detail/(?P<pk>\d+)/$', views.peripheral_detail, name='peripheral_detail'),
	url(r'^peripheral/(?P<pk>\d+)/remove/$', views.peripheral_remove, name='peripheral_remove'),
	url(r'^peripheral/datatable/$', views.peripheral_list, name='peripheral_datatable'),
	url(r'^peripheral/actuador/(?P<pk>\d+)/$', views.peripheral_actuador, name='peripheral_actuador'),
	url(r'^weather/station/$', views.weather_station, name='weather_station'),
	url(r'^broker/new/$', views.broker_new, name='broker_new'),
	url(r'^broker/detail/$', views.broker_detail, name='broker_detail'),
	url(r'^broker/new/$', views.broker_remove, name='broker_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)