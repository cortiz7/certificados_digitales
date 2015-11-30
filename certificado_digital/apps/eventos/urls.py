from django.conf.urls import include, url
from .views import IndexView, MainPanelView, buscar

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"),
	url(r'^panel/$', MainPanelView.as_view(), name="panel"),
	url(r'^buscar/$', buscar, name="buscar"),
	#url(r'^panel/evento/nuevo/$', CreateEvento.as_view(), name="nuevo"),
	# url(r'^panel/evento/(?P<pk>\d+)/$', DetailEvento.as_view(), name="detalle"),
	# url(r'^panel/evento/editar/(?P<pk>\d+)/$', EditEvento.as_view(), name="editar"),
	# url(r'^panel/evento/eliminar/(?P<pk>\d+)/$', DeleteEvento.as_view(), name="eliminar"),
]
