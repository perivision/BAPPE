from django import forms

class InventoryForm(forms.Form):
	item_name = forms.CharField(label='name', required=True, max_length=128) 
	item_count = forms.CharField(label='number of items', required=True, max_length=128) 
	item_location = forms.CharField(label='location of item', required=True, max_length=128) 
	item_count_type = forms.CharField(label='count type', required=True, max_length=128) 
	action_date = forms.DateField(label='date')
	action_type = forms.CharField(label='action type', required=True, max_length=128) 
	action_auther = forms.CharField(label='author', required=True, max_length=128) 
	action_contact = forms.CharField(label='contact', required=True, max_length=128) 
	item_in_transit = forms.BooleanField(label='is item in transit?', required=False, initial=False)
