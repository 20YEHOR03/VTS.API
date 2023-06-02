from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..services.bracelet_service import *
from ..permissions import IsAdminCustomUser, HasOrganization

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def bracelet_create_and_list(request):
    if request.method == 'GET':
        return get_bracelets(request)
    elif request.method == 'POST':
        return create_bracelet(JSONParser().parse(request), request)

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated & IsAdminCustomUser & HasOrganization])
def bracelet_rud(request, bracelet_id):
    if request.method == 'GET':
        return get_bracelet(bracelet_id, request)
    elif request.method == 'PATCH':
        return update_bracelet(bracelet_id, JSONParser().parse(request), request)
    elif request.method == 'DELETE':
       return delete_bracelet(bracelet_id, request)