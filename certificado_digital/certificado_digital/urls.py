from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.eventos.urls', namespace="eventos_app")),
	# url(r'^', include('apps.certificados.urls', namespace="certificados_app")),
 #    url(r'^', include('apps.usuarios.urls', namespace="usuaurios_app")),
     url(r'^admin/', include(admin.site.urls)),
]
