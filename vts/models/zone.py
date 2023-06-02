from django.db import models
from .organization import Organization

class Zone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)