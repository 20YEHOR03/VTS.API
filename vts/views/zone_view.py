from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..services.zone_service import *
from ..permissions import IsAdminCustomUser, HasOrganization

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def zone_create_and_get_list(request):
    if request.method == 'POST':
        return create_zone(JSONParser().parse(request), request)
    elif request.method == 'GET':
        return get_zones(request)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def zone_rud(request, zone_id):
    if request.method == 'GET':
        return get_zone(request, zone_id)
    elif request.method == 'PUT':
        return update_zone(zone_id, JSONParser().parse(request), request)
    elif request.method == 'DELETE':
        return delete_zone(zone_id, request)