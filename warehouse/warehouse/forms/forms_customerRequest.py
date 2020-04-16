from django import forms

class CustomerRequest(forms.Form):
	name = forms.CharField(label='name',required=True, max_length=128) 
	email = forms.EmailField(label='email', required=True, max_length=128)
	phone = forms.CharField(label='phone', required=True, max_length=13)
	role = forms.CharField(label='role', required=True, max_length=128)
	location = forms.CharField(label='location', required=True, max_length=128)
	organization = forms.CharField(label='organization', required=True, max_length=128)
