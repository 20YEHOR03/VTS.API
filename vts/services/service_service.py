from ..models.service import Service
from ..serializers.service_serializer import ServiceSerializer
from rest_framework import status
from rest_framework.response import Response

def get_service(service_id, request):
    try:
        instance = Service.objects.get(pk=service_id)
        if request.user.organization_id != instance.organization_id:
            return Response({'message': "User can get services only of his/her organization"}, status.HTTP_403_FORBIDDEN)
        serializer = ServiceSerializer(instance)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_service_by_service_id(service_id):
    try:
        instance = Service.objects.get(pk=service_id)
        serializer = ServiceSerializer(instance)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_services(request):
    organization_id = request.user.organization_id
    services = Service.objects.filter(organization_id=organization_id)
    serializer = ServiceSerializer(services, many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_services_by_zone_id(zone_id, request):
    organization_id = request.user.organization_id
    services = Service.objects.filter(zone_id=zone_id)
    serializer = ServiceSerializer(services, many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    if serializer.data[0].get('organization_id') != organization_id:
        return Response({'message': "User can get services only of his/her organization"}, status.HTTP_403_FORBIDDEN)
    
    return Response(serializer.data, status.HTTP_200_OK)

def create_service(data, request):
    organization_id = request.user.organization_id
    data["organization_id"] = organization_id
    serializer = ServiceSerializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()            
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_service(service_id, data, request):
    try:
        service = Service.objects.get(pk=service_id)

    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    if request.user.organization_id != service.organization_id:
        return Response({'message': "User can update services only of his/her organization"}, status.HTTP_403_FORBIDDEN)
    data["organization_id"] = service.organization_id
    serializer = ServiceSerializer(service, data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            print(str(e))
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_service(service_id, request):
    try:
        service = Service.objects.get(pk=service_id)
        
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    if request.user.organization_id != service.organization_id:
        return Response({'message': "User can delete services only of his/her organization"}, status.HTTP_403_FORBIDDEN)
    try:
        service.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_204_NO_CONTENT)