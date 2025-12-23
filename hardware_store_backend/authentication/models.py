from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    """
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # For hardware store customers
    is_verified = models.BooleanField(default=False)
    company_name = models.CharField(max_length=200, blank=True)  # For business customers
    tax_id = models.CharField(max_length=50, blank=True)  # For business customers
    
    def __str__(self):
        return self.email or self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
