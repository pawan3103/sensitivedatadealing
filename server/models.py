from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from phonenumber_field.modelfields import PhoneNumberField
from fernet_fields import EncryptedTextField, EncryptedField


class PhoneEncryptedField(EncryptedField, PhoneNumberField):
    pass


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	country = models.CharField(max_length=128, null=True)
	phone_number = PhoneNumberField(null=True)
	# passport_number = models.TextField(null=True)
	passport_number = EncryptedTextField(null=True)
	encrypted_phone_number = PhoneEncryptedField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)