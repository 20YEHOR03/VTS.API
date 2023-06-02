from django.urls import path
from ..views.interaction_view import *

urlpatterns = [
    path('', interaction_create),
    path('<int:interaction_id>', interaction_get),
    path('get-full-list', interaction_get_list),
    path('get-user-list', interaction_get_user_list),
    path('get-zone-list/<int:zone_id>', interaction_get_zone_list),
    path('get-service-list/<int:service_id>', interaction_get_service_list)
]