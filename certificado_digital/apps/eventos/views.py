from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category, Certificate
from .forms import EventoForm, SearchForm
# from apps.users.models import Usuario

from django.core.urlresolvers import reverse, reverse_lazy


from django.views.generic import TemplateView

class IndexView(TemplateView):

	template_name = 'eventos/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['events'] = Event.objects.all().order_by('-created')[:6]
		return context




class MainPanelView(TemplateView):

	template_name = 'eventos/panel/panel.html'

def buscar(request):
  form_buscar = SearchForm()
  if request.method == "POST":    
    if 'buscar_codigo_form' in request.POST:
      search_form = SearchForm(request.POST)
      if search_form.is_valid():
        q = search_form.cleaned_data['name']
        certificates = Certificate.objects.filter(guid=q)
        return render(request, 'eventos/resultados.html',{'certificates': certificates,})
      else:
        return render(request, 'eventos/index.html', {'form_buscar' : form_buscar})
  else:
    return render(request, 'eventos/index.html', {'form_buscar' : form_buscar})