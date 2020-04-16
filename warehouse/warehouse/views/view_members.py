from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..customModels.models import CustomUser

@login_required
def viewMembers(request):
  if request.method == 'GET':
    # TODO show inventory
    items = CustomUser.objects.all()
    return render(request, 'showmembers.html', {'items': items})