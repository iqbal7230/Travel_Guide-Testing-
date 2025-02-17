# from django.db import models
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    
    class Meta:
        db_table = 'travel_guide_customer' 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
