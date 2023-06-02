from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..services.interaction_service import *
from ..permissions import IsAdminCustomUser, HasOrganization

@api_view(['POST'])
def interaction_create(request):
    if request.method == 'POST':
        return create_interaction(JSONParser().parse(request))

@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def interaction_get_list(request):
    if request.method == 'GET':
        return get_interaction_list(request)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def interaction_get_user_list(request):
    if request.method == 'GET':
        return get_interaction_list(request)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def interaction_get_zone_list(request, zone_id):
    if request.method == 'GET':
        return get_interaction_list_by_id(zone_id, request)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def interaction_get_service_list(request, service_id):
    if request.method == 'GET':
        return get_interaction_list_by_id(service_id, request)

@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def interaction_get(request, interaction_id):
    if request.method == 'GET':
        return get_interaction(interaction_id, request)