from django.db import models
from django.contrib.auth.models import User

# Contact model that represents an entry in a user's contact list.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_app_contacts')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
