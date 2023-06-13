from django.urls import path
from ..views.customuser_view import *
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', views.obtain_auth_token),
    path('create-visitor/', create_visitor),
    path('get-access-info/<str:rfid>', get_access_info),
    path('get-info/', get_customuser_info),
    path('get-info/<int:customuser_id>', get_visitor_info),
    path('update-info/', update_customuser_info),
    path('update-info/<int:customuser_id>', update_visitor_info),
    path('deactivate-info/<int:customuser_id>', deactivate_visitor_info),
    path('get-actual-visitors/', get_actual_visitors),
    path('get-visitors/', get_all_visitors)
]