from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Customer(AbstractUser):
    phone = models.CharField(max_length=20,blank=True , null=True)
    address = models.TextField(blank=True , null=True)
    
    def __str__(self):
        return self.username