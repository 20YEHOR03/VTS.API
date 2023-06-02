from ..models.zone import Zone
from ..serializers.zone_serializer import ZoneSerializer
from rest_framework import status
from rest_framework.response import Response

def get_zone(request, zone_id):
    try:
        instance = Zone.objects.get(pk=zone_id)
        if request.user.organization_id != instance.organization_id:
            return Response({'message': "User can get zones only of his/her organization"}, status.HTTP_403_FORBIDDEN)
        serializer = ZoneSerializer(instance)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_zones(request):
    organization_id = request.user.organization_id
    zones = Zone.objects.filter(organization_id=organization_id)
    serializer = ZoneSerializer(zones, many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def create_zone(data, request):
    organization_id = request.user.organization_id
    data["organization_id"] = organization_id
    serializer = ZoneSerializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()            
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_zone(zone_id, data, request):
    try:
        zone = Zone.objects.get(pk=zone_id)
        if request.user.organization_id != zone.organization_id:
            return Response({'message': "User can update zones only of his/her organization"}, status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    data["organization_id"] = zone.organization_id
    serializer = ZoneSerializer(zone, data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_zone(zone_id, request):

    try:
        zone = Zone.objects.get(pk=zone_id)
        if request.user.organization_id != zone.organization_id:
            return Response({'message': "User can delete zones only of his/her organization"}, status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    try:
        zone.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_204_NO_CONTENT)