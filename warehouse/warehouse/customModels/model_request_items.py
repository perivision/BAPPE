from django.db import models

class RequestItemModel(models.Model):
	item_id = models.AutoField(primary_key=True)
	date = models.DateField(("Date"))
	item_count = models.IntegerField()
	customer = models.CharField(max_length=128)
	member = models.CharField(max_length=128)
	location = models.CharField(max_length=128)