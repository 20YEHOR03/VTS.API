from .bracelet import Bracelet
from .customuser import CustomUser
from .gender import Gender
from .interaction import Interaction
from .organization import Organization
from .role import Role
from .service import Service
from .zone import Zone

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)