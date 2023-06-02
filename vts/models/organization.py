from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)