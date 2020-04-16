from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms.forms_request_items import RequestItemsForm
from ..customModels.model_request_items import RequestItemModel

@login_required
def requestItems(request):
  if request.method == 'POST':
    form = RequestItemsForm(request.POST)
    if form.is_valid():
      requestItem = RequestItemModel()
      requestItem.item_count = form.cleaned_data.get('item_count')
      requestItem.location = form.cleaned_data.get('location')
      requestItem.member = form.cleaned_data.get('member_id')
      requestItem.customer = form.cleaned_data.get('customer_id')
      requestItem.date = form.cleaned_data.get('date')
      requestItem.save()
      return HttpResponseRedirect('/dashboard')
  else:
    form = RequestItemsForm()
  return render(request, 'requestitems.html', {'form': form})

@login_required
def showRequests(request):
  if request.method == 'GET':
    items = RequestItemModel.objects.exclude(item_count=0)
    return render(request, 'showrequests.html', {'items': items})