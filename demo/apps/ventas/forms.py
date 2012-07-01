from django import forms

class addProductForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data


