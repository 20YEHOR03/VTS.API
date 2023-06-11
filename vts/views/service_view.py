from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..services.service_service import *
from ..permissions import IsAdminCustomUser, HasOrganization

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def service_create_and_get_list(request):
    if request.method == 'POST':
        return create_service(JSONParser().parse(request), request)
    elif request.method == 'GET':
        return get_services(request)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def service_rud(request, service_id):
    if request.method == 'GET':
        return get_service(service_id, request)
    elif request.method == 'PUT':
        return update_service(service_id, JSONParser().parse(request), request)
    elif request.method == 'DELETE':
       return delete_service(service_id, request)

@api_view(['GET'])
def service_by_service_id(request, service_id):
    if request.method == 'GET':
        return get_service_by_service_id(service_id)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def service_by_zone_id(request, zone_id):
    if request.method == 'GET':
        return get_services_by_zone_id(zone_id, request)