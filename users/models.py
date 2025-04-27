from django.db import models
from django.contrib.auth.models import User


# profile model extends the default user model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices = (("Male","Male"), ("Female", "Female"), ("Others", "Others")) ,null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username


# Contact model stores a user’s contact information.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_app_contacts')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=100, blank=True)
    phone_numbers = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"