from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Contact (models.Model):
    
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=13)
    desc=models.TextField(max_length=2000)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + "   "+ str(self.date)
  