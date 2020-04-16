from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

class CustomBackend(BaseBackend):
	def authenticate(self, request, username=None, password=None):
		userModel = get_user_model()
		try:
			user = userModel.objects.get(email=username)
		except:
			return None
		if user is not None:
			if user.check_password(password):
				return user
		return None

# def authenticate(self, request, token=None):
# 	# TODO auth based on token
# 	print()    	
