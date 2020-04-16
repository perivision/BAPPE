from django.db import models

class ItemGivenModel(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_count = models.IntegerField()
	date = models.DateField(("Date"))
	customer = models.CharField(max_length=128)
	member = models.CharField(max_length=128)
	location = models.CharField(max_length=128)