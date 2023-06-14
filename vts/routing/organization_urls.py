from django.urls import path
from ..views.organization_view import *

urlpatterns = [
    path('', organization_create, name="organization_create"),
    path('statistics/<int:organization_id>', organization_get_statistics, name="organization_get_statistics"),
    path('<int:organization_id>', organization_rud, name="organization_rud"),
    path('statistics/get-report/<int:organization_id>', generate_report, name="generate_report")
]