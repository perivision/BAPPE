from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
	customer_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	email = models.EmailField(max_length=128)
	# TODO fix phone invalid - also good to show example placeholder
	phone = PhoneNumberField()
	role = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	organization = models.CharField(max_length=128)