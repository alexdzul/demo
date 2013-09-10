from django import forms
from demo.apps.ventas.models import producto

class addProductForm(forms.ModelForm):
	class Meta:
		model   = producto
		exclude = {'status',}

"""
class addProductForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.TextInput())
	imagen 		= forms.ImageField(required=False)
	precio		= forms.DecimalField(required=True)
	stock		= forms.IntegerField(required=True)

	def clean(self):
		return self.cleaned_data
"""