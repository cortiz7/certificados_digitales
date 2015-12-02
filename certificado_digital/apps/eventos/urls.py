from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^panel/$', views.MainPanelView.as_view(), name="panel"),	
	url(r'^busqueda_certificado/$', views.busqueda_certificado, name="busqueda_certificado"),
	#url(r'^panel/evento/nuevo/$', CreateEvento.as_view(), name="nuevo"),
	# url(r'^panel/evento/(?P<pk>\d+)/$', DetailEvento.as_view(), name="detalle"),
	# url(r'^panel/evento/editar/(?P<pk>\d+)/$', EditEvento.as_view(), name="editar"),
	# url(r'^panel/evento/eliminar/(?P<pk>\d+)/$', DeleteEvento.as_view(), name="eliminar"),
]
