from django.db import models
from .customuser import CustomUser
from .service import Service

class Interaction(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    interaction_datetime = models.DateTimeField()
    info = models.CharField(null=True)