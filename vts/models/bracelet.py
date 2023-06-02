from django.db import models
from .customuser import CustomUser
from .organization import Organization

class Bracelet(models.Model):
    rfid = models.CharField(max_length=100, unique=True)
    status = models.BooleanField()
    activation_date = models.DateField()
    deactivation_date = models.DateField()
    customuser = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, default=None)