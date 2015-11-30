from django import forms
from .models import Event

class EventoForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('views', 'organizer', 'created', 'modified')
		widgets = {
			'name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'summary': forms.Textarea(attrs={'class' : 'form-control', 'rows' : '2'}),
			'content': forms.Textarea(attrs={'class' : 'form-control', 'rows' : '2'}),
			'category': forms.Select(attrs={'class' : 'form-control'}),
			'place': forms.TextInput(attrs={'class' : 'form-control'}),
			'start': forms.DateTimeInput(attrs={'class' : 'form-control'}),
			'finish': forms.DateTimeInput(attrs={'class' : 'form-control'}),
			'imagen': forms.ClearableFileInput(attrs={'class' : 'form-control'}),
			'is_free': forms.CheckboxInput(),
			'amount': forms.NumberInput(attrs={'class' : 'form-control'}),
		}

class SearchForm(forms.Form):
	name = forms.CharField(max_length=13,
		widget = forms.TextInput(attrs = {
			'class' : 'form-control', 
			'placeholder' : 'Ingresa Codigo de Verificacion',
			'autocomplete' : 'off',
			}))