from django import forms

class RequestItemsForm(forms.Form):
	# TODO need item name?
	item_count = forms.CharField(label='count', required=True, max_length=128)
	date = forms.DateField(label='date', required=True)
	# TODO these are auto populated?
	customer_id = forms.CharField(label='customer', required=True, max_length=128) 
	member_id = forms.CharField(label='member', required=True, max_length=128) 
	location = forms.CharField(label='location', required=True, max_length=128) 