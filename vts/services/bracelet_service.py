from ..models.bracelet import Bracelet
from ..serializers.bracelet_serializer import BraceletSerializer
from rest_framework import status
from rest_framework.response import Response

def get_bracelet(bracelet_id, request):
    try:
        organization_id = request.user.organization_id
        bracelet = Bracelet.objects.get(pk=bracelet_id)
        if bracelet.organization_id != organization_id:
            return Response({'message': "User can update bracelets only his/her organization"}, status.HTTP_403_FORBIDDEN)
        bracelet_serializer = BraceletSerializer(bracelet)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(bracelet_serializer.data, status.HTTP_200_OK)

def get_bracelets(request):
    organization_id = request.user.organization_id
    bracelets = Bracelet.objects.filter(organization_id=organization_id)
    serializer = BraceletSerializer(bracelets, many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def create_bracelet(data, request):
    organization_id = int(request.user.organization_id)
    data['status'] = True
    data['organization_id'] = organization_id
    serializer = BraceletSerializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_bracelet(bracelet_id, data, request):
    organization_id = request.user.organization_id
    try:
        bracelet = Bracelet.objects.get(pk=bracelet_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    if bracelet.organization_id != organization_id:
        return Response({'message': "User can update bracelets only his/her organization"}, status.HTTP_403_FORBIDDEN)
    serializer = BraceletSerializer(bracelet, data=data, partial=True)
    
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# def update_bracelet(bracelet_id, data, request):
#     organization_id = request.user.organization_id
#     try:
#         bracelet = Bracelet.objects.get(pk=bracelet_id)
#     except Exception as e:
#         print(f"Exception occurred: {str(e)}")
#         return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
#     if bracelet.organization_id != organization_id:
#         print("User does not have permission to update bracelets")
#         return Response({'message': "User can update bracelets only in his/her organization"}, status.HTTP_403_FORBIDDEN)
    
#     serializer = BraceletSerializer(bracelet, data=data, partial=True)
#     if serializer.is_valid():
#         try:
#             serializer.save()
#             print("Bracelet saved successfully")
#             return Response(serializer.data, status.HTTP_200_OK)
#         except Exception as e:
#             print(f"Exception occurred while saving bracelet: {str(e)}")
#             return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
#     else:
#         print("Serializer is not valid")
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_bracelet(bracelet_id, request):
    organization_id = request.user.organization_id
    try:
        bracelet = Bracelet.objects.get(pk=bracelet_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    if bracelet.organization_id != organization_id:
        return Response({'message': "User can delete bracelets only his/her organization"}, status.HTTP_403_FORBIDDEN)
    try:
        bracelet.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_204_NO_CONTENT)