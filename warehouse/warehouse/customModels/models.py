from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager

class CustomUser(AbstractUser):
	member_id = models.AutoField(primary_key=True)
	username = None
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70, unique= True)
	# TODO fix phone invalid - also good to show example placeholder
	phone = PhoneNumberField()
	role = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	slackId = models.CharField(max_length=30)
	objects = CustomUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email

	@receiver(post_save, sender=AbstractUser)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=AbstractUser)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
