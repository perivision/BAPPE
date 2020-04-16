from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms.forms_customerRequest import CustomerRequest
from ..customModels.model_customer import Customer

@login_required
def customer(request):
  if request.method == 'POST':
    form = CustomerRequest(request.POST)
    if form.is_valid():
      customer = Customer()
      customer.name = form.cleaned_data.get('name')
      customer.email = form.cleaned_data.get('email')
      customer.phone = form.cleaned_data.get('phone')
      customer.role = form.cleaned_data.get('role')
      customer.location = form.cleaned_data.get('location')
      customer.organization = form.cleaned_data.get('organization')
      customer.save()
      return HttpResponseRedirect('/dashboard')
  else:
    form = CustomerRequest()

  return render(request, 'customer.html', {'form': form})

@login_required
def viewCustomers(request):
  if request.method == 'GET':
    # TODO show inventory
    items = Customer.objects.all()
    return render(request, 'showcustomers.html', {'items': items})