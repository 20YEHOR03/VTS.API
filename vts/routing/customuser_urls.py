from django.urls import path
from ..views.customuser_view import *
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', views.obtain_auth_token),
    path('create-visitor/', create_visitor),
    path('get-access-info/<str:rfid>', get_access_info),
    path('get-info/', get_customuser_info),
    path('get-actual-visitors/', get_actual_visitors)
]