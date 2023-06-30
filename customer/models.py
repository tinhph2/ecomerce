from django.db import models


# Create your models here.
from django.db import models
from django.urls import reverse
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, db_index=True)
    phone = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=250)