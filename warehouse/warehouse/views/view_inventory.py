from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms.forms_inventory import InventoryForm
from ..customModels.model_inventory import InventoryModel

@login_required
def addInventory(request):
  # TODO add update here also
  if request.method == 'POST':
    form = InventoryForm(request.POST)
    if form.is_valid():
      inventory = InventoryModel()
      inventory.item_name = form.cleaned_data.get('item_name')
      inventory.item_count = form.cleaned_data.get('item_count')
      inventory.item_location = form.cleaned_data.get('item_location')
      inventory.item_count_type = form.cleaned_data.get('item_count_type')
      inventory.action_date = form.cleaned_data.get('action_date')
      inventory.action_type = form.cleaned_data.get('action_type')
      inventory.action_author = form.cleaned_data.get('action_author')
      inventory.action_contact = form.cleaned_data.get('action_contact')
      inventory.item_in_transit = form.cleaned_data.get('item_in_transit')
      inventory.save()
      return HttpResponseRedirect('/dashboard')
  else:
    form = InventoryForm()
  return render(request, 'inventory.html', {'form': form})


@login_required
def editInventory(request, itemId):
  if request.method == 'GET':
    items = InventoryModel.objects.get(itemId)
    form = InventoryForm(initial= {
      'item_id': items.item_id,
      'item_name': items.item_name,
      'item_count': items.item_count,
      'item_location': items.item_location,
      'item_count_type': items.item_count_type,
      'action_date': items.action_date,
      'action_type': items.action_type,
      'action_author': items.action_author,
      'action_contact': items.action_contact,
      'item_in_transit': items.item_in_transit
    });
    return render(request, 'showinventory.html', {'form': form})

@login_required
def viewInventory(request):
  if request.method == 'GET':
    items = InventoryModel.objects.all()
    return render(request, 'showinventory.html', {'items': items})

@login_required
def inTransit(request):
  if request.method == 'GET':
    # TODO show inventory
    items = InventoryModel.objects.exclude(item_in_transit=0)
    return render(request, 'showintransit.html', {'items': items})

