from django.urls import path
from ..views.service_view import *

urlpatterns = [
    path('', service_create_and_get_list),
    path('<int:service_id>', service_rud),
    path('get-by-zone-id/<int:zone_id>', service_by_zone_id),
]