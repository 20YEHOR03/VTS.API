from django.urls import path
from ..views.zone_view import *

urlpatterns = [
    path('', zone_create_and_get_list),
    path('<int:zone_id>', zone_rud, name='zone_rud'),
]