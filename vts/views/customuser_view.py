from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..services.customuser_service import *
from ..permissions import IsAdminCustomUser, HasOrganization

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

@api_view(['POST'])
def register(request):
    return register_customuser(JSONParser().parse(request))

@api_view(['POST'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def create_visitor(request):
    return create_visitor_by_admin(JSONParser().parse(request), request)

@api_view(['GET'])
def get_access_info(request, rfid):
    return get_info_access(rfid)

@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def get_actual_visitors(request):
    return get_visitors_actual(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def get_all_visitors(request):
    return get_visitors(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated & HasOrganization])
def get_customuser_info(request):
    return get_own_info(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def get_visitor_info(request, customuser_id):
    return get_info(customuser_id, request)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated & HasOrganization])
def update_customuser_info(request):
    return update_customuser(JSONParser().parse(request), request)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def update_visitor_info(request, customuser_id):
    return update_customuser(customuser_id, JSONParser().parse(request), request)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def deactivate_visitor_info(request, customuser_id):
    return deactivate_customuser(customuser_id, JSONParser().parse(request), request)