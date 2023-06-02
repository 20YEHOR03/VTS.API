from django.db import models
from .organization import Organization
from .gender import Gender
from .role import Role
from .zone import Zone

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    minimum_age = models.IntegerField(default=0)
    allowed_genders = models.ManyToManyField(Gender, related_name='allowed_services')
    allowed_roles = models.ManyToManyField(Role, related_name='allowed_roles')
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)