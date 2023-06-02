from ..models.organization import Organization
from ..serializers.organization_serializer import OrganizationSerializer
from rest_framework import status
from rest_framework.response import Response

def get_organization(organization_id, request):
    if request.user.organization_id != organization_id:
        return Response({'message': "User can get only his/her organization"}, status.HTTP_403_FORBIDDEN)
    try:
        instance = Organization.objects.get(pk=organization_id)
        organization_serializer = OrganizationSerializer(instance)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(organization_serializer.data, status.HTTP_200_OK)

def get_organizations():
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def create_organization(data):
    serializer = OrganizationSerializer(data=data)
    
    if serializer.is_valid():
        try:
            serializer.save()            
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_organization(organization_id, data, request):
    if request.user.organization_id != organization_id:
        return Response({'message': "User can update only his/her organization"}, status.HTTP_403_FORBIDDEN)
    try:
        organization = Organization.objects.get(pk=organization_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    serializer = OrganizationSerializer(organization, data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_organization(organization_id, request):
    if request.user.organization_id != organization_id:
        return Response({'message': "User can delete only his/her organization"}, status.HTTP_403_FORBIDDEN)
    try:
        organization = Organization.objects.get(pk=organization_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    try:
        organization.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_204_NO_CONTENT)