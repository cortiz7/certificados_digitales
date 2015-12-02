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
        response = JsonResponse({'guid' : 'dd'})
        print(codigo_guid)
        return HttpResponse(response.content)
    else:
        return redirect('/')



class IndexView1(TemplateView):
    template_name = 'eventos/index.html'
  #form_class = SearchForm

  # def get_context_data(self, **kwargs):
	# 	context = super(IndexView, self).get_context_data(**kwargs)
	# 	context['events'] = Event.objects.all().order_by('-created')[:6]
	# 	return context


class IndexView(View):
    form_class = SearchForm
    initial = {'key': 'value'}
    template_name = 'eventos/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form_buscar': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     dato = "pppp"
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         form = self.form_class(initial=self.initial)
    #         return render(request, self.template_name, {'form_buscar': form, 'dato': dato})

    #     return render(request, self.template_name, {'form_buscar': form})

class MainPanelView(TemplateView):

	template_name = 'eventos/panel/panel.html'

def buscar(request):
  form_buscar = SearchForm()
  if request.method == "POST":
    if 'b_codigo' in request.POST:
      search_form = SearchForm(request.POST)
      if search_form.is_valid():
        q = search_form.cleaned_data['codigo']
        certificates = Certificate.objects.filter(guid=q)
        return render(request, 'eventos/resultados.html',{'certificates': certificates,})
      else:
        return render(request, 'eventos/index.html', {'form_buscar' : form_buscar})
  else:
    return render(request, 'eventos/index.html', {'form_buscar' : form_buscar})
