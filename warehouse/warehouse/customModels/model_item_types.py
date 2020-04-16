from django.db import models

class ItemTypesModel(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_type = models.CharField(max_length=128)
	item_subtype = models.CharField(max_length=128)
	doc_link = models.CharField(max_length=128)
	notes = models.TextField()