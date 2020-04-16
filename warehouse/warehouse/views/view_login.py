from django.contrib.auth import login, authenticate
#from django.contrib.auth.backends import CustomBackend
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms.forms_login import LoginForm

def getLogin(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=email, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {email}")
        return HttpResponseRedirect('/dashboard/')
      else:
        messages.error(request, "Invalid username or password.")
  else:
    form = LoginForm()

  return render(request, 'login.html', {'form': form})