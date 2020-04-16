# import model_members?
from django import forms

from ..customModels.models import CustomUser
from .forms import CustomUserCreationForm

class SignupForm(CustomUserCreationForm):
	name = forms.CharField(label='name', required=True, max_length=30)
	phone = forms.CharField(label='phone', required=True, max_length=13)
	role = forms.CharField(label='role', required=True, max_length=30)
	location = forms.CharField(label='location', required=True, max_length=30)
	slackId = forms.CharField(label='slack Id', required=True, max_length=30)

	class Meta:
		model = CustomUser
		fields = ('email', 'name', 'phone', 'role', 'location', 'slackId',)