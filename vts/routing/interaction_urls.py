from django.urls import path
from ..views.interaction_view import *

urlpatterns = [
    path('', interaction_create),
    path('<int:interaction_id>', interaction_get),
    path('get-full-list', interaction_get_list),
    path('get-user-list', interaction_get_user_list),
    path('get-zones-statistics', interaction_get_zones_statistics),
    path('get-services-statistics', interaction_get_services_statistics)
]