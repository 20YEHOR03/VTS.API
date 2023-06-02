from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..permissions import IsAdminCustomUser, HasOrganization
from ..services.organization_service import *

@api_view(['POST'])
def organization_create(request):
    if request.method == 'POST':
        return create_organization(JSONParser().parse(request))

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def organization_rud(request, organization_id):
    if request.method == 'GET':
        return get_organization(organization_id, request)
    elif request.method == 'PUT':
        return update_organization(organization_id, JSONParser().parse(request), request)
    elif request.method == 'DELETE':
       return delete_organization(organization_id, request)