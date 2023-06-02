from django.urls import path
from ..views.organization_view import *

urlpatterns = [
    path('', organization_create),
    path('<int:organization_id>', organization_rud),
]