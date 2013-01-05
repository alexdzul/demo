from django import forms

class addProductForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.TextInput())
	imagen 		= forms.ImageField(required=False)
	precio		= forms.DecimalField(required=True)
	stock		= forms.IntegerField(required=True)

	def clean(self):
		return self.cleaned_data


