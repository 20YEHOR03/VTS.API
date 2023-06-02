from django.urls import path
from ..views.customuser_view import *

urlpatterns = [
    path('register/', register),
    path('create_visitor/', create_visitor),
    path('get-access-info/<str:rfid>', get_access_info),
    path('get-info/', get_customuser_info),
    path('get-actual-visitors/', get_actual_visitors)
]