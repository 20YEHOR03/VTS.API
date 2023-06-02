from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from ..services.customuser_service import *
from ..permissions import IsAdminCustomUser, HasOrganization

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
@permission_classes([IsAuthenticated & HasOrganization])
def get_customuser_info(request):
    return get_info(request)