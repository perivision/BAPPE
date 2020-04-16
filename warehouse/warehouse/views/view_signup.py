from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms.forms_signup import SignupForm
from ..customModels.models import CustomUser

def getSignup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # TODO check if passwords match
            rawPassword = form.cleaned_data.get('password1')
            verfiyPassword = form.cleaned_data.get('password2')
            user = CustomUser()
            user.name = form.cleaned_data.get('name')
            user.email = form.cleaned_data.get('email')
            user.set_password(rawPassword)
            user.phone = form.cleaned_data.get('phone')
            user.role = form.cleaned_data.get('role')
            user.location = form.cleaned_data.get('location')
            user.slackId = form.cleaned_data.get('slackId')
            user.save()
            return HttpResponseRedirect('/signupSuccess')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})