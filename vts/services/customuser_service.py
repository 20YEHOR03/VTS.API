from rest_framework.response import Response
from rest_framework import status
from ..serializers.customuser_serializer import CustomUserSerializer, SafeCustomUserSerializer
from ..serializers.access_info_serializer import AccessInfoSerializer
from ..models import Role, Bracelet, CustomUser

def register_customuser(data):
    role = Role.objects.get(name="admin")
    data["role_id"] = role.id
    data["is_staff"] = True
    serializer = CustomUserSerializer(data=data)
    
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def create_visitor_by_admin(data, request):
    role = Role.objects.get(name="visitor")
    organization_id = request.user.organization_id
    data["role_id"] = role.id
    data["organization_id"] = organization_id
    data["is_staff"] = False
    serializer = CustomUserSerializer(data=data)
    
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def get_info_access(rfid):
    try:
        bracelet = Bracelet.objects.get(rfid=rfid)
        user = CustomUser.objects.get(bracelet=bracelet.id)
        access_info_serializer = AccessInfoSerializer(user)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(access_info_serializer.data, status.HTTP_200_OK)

def get_visitors_actual(request):
    organization_id = request.user.organization_id
    all_bracelets = Bracelet.objects.filter(organization_id=organization_id)
    actual_bracelets = all_bracelets.filter(status=True)
    user_ids = actual_bracelets.values('customuser_id')
    all_users = CustomUser.objects.filter(id__in=user_ids)
    visitors = all_users.filter(role_id=2)
    serializer = SafeCustomUserSerializer(visitors.filter(is_active=True), many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_visitors(request):
    organization_id = request.user.organization_id
    all_users = CustomUser.objects.filter(organization_id=organization_id)
    visitors = all_users.filter(role_id=2)
    serializer = SafeCustomUserSerializer(visitors.filter(is_active=True), many = True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_own_info(request):
    try:
        id = request.user.id
        user = CustomUser.objects.get(pk=id)
        serializer = SafeCustomUserSerializer(user)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def get_info(customuser_id, request):
    try:
        user = CustomUser.objects.get(pk=customuser_id)
        serializer = SafeCustomUserSerializer(user)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status.HTTP_200_OK)

def update_customuser(data, request):
    try:
        user = CustomUser.objects.get(pk=user.id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    serializer = CustomUserSerializer(user, data=data, partial=True)
    
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_customuser(customuser_id, data, request):
    organization_id = request.user.organization_id
    try:
        user = CustomUser.objects.get(pk=customuser_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    if user.organization_id != organization_id:
        return Response({'message': "User can update visitors only his/her organization"}, status.HTTP_403_FORBIDDEN)
    serializer = CustomUserSerializer(user, data=data, partial=True)
    
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def deactivate_customuser(customuser_id, data, request):
    try:
        customuser = CustomUser.objects.get(pk=customuser_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    if request.user.organization_id != customuser.organization_id:
        return Response({'message': "User can delete visitors only of his/her organization"}, status.HTTP_403_FORBIDDEN)
    data['is_active'] = False
    serializer = CustomUserSerializer(customuser, data=data, partial=True)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)