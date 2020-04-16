from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..customModels.model_customer import Customer
from ..customModels.models import CustomUser
from ..customModels.model_inventory import InventoryModel
from ..customModels.model_request_items import RequestItemModel

@login_required
def dashboard(request):
	if request.method == 'GET':
		itemRequests = RequestItemModel.objects.exclude(item_count=0).order_by('-item_id')[:10]
		inventory = InventoryModel.objects.all()[:10]
		inTransit = InventoryModel.objects.exclude(item_in_transit=0)[:10]
		members = CustomUser.objects.all()[:10]
		customers = Customer.objects.all()[:10]
		return render(request, 'dashboard.html', {
			'itemRequests': itemRequests,
			'inTransit': inTransit,
			'inventory': inventory,
			'members': members,
			'customers': customers
			})