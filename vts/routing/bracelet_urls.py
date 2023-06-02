from django.urls import path
from ..views.bracelet_view import *

urlpatterns = [
    path('', bracelet_create_and_list),
    path('<int:bracelet_id>', bracelet_rud)
]