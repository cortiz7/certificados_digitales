#encoding:utf-8

from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category, Certificate
from .forms import EventoForm, SearchForm
from django.http import HttpResponseRedirect, HttpResponse

from django.http import JsonResponse
# from apps.users.models import Usuario

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import View, TemplateView



def busqueda_certificado(request):

    if request.is_ajax():
        codigo = request.GET['codigo_certificado']        
        try:
            certi = get_object_or_404(Certificate, guid=codigo)
        except:
            certi = 0

        if certi :            
            data = {
                'guid' : certi.guid,
                'evento' : certi.event.name,
                }
        else:
            data = {
                'encontrado' : 'False'
                }
        response = JsonResponse(data)
        return HttpResponse(response.content)
    else:
        return redirect('/')

class IndexView(View):
    form_class = SearchForm
    initial = {'key': 'value'}
    template_name = 'eventos/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form_buscar': form})

class MainPanelView(TemplateView):

	template_name = 'eventos/panel/panel.html'
