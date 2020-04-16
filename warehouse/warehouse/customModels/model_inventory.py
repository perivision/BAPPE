from django.db import models

class InventoryModel(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_name = models.CharField(max_length=128)
	item_count = models.IntegerField()
	item_location = models.CharField(max_length=128)
	item_count_type = models.CharField(max_length=128)
	action_date = models.DateField(("Date"))
	action_type = models.CharField(max_length=128)
	action_author = models.CharField(max_length=128)
	action_contact = models.CharField(max_length=128)
	item_in_transit = models.BooleanField(default=False)