from ..models.interaction import Interaction
from ..serializers.interaction_serializer import InteractionSerializer, SafeInteractionSerializer
from rest_framework import status
from rest_framework.response import Response
from ..models import CustomUser, Service

def get_interaction(interaction_id, request):
    try:
        customuser_id = request.user.id
        interaction = Interaction.objects.get(pk=interaction_id)
        if interaction.customuser_id != customuser_id:
            return Response({'message': "User can get interactions only his/her organization"}, status.HTTP_403_FORBIDDEN)
        interaction_serializer = InteractionSerializer(interaction)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_204_NO_CONTENT)
    return Response(interaction_serializer.data, status.HTTP_200_OK)

def get_interaction_list(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if request.path.split("?")[0] == '/interaction/get-full-list':
        organization_id = request.user.organization_id
        interactions = Interaction.objects.filter(service__organization_id=organization_id)
    elif request.path.split("?")[0] == '/interaction/get-user-list':
        customuser_id = request.user.id
        interactions = Interaction.objects.filter(customuser_id=customuser_id)
    if start_date and end_date:
        interactions = interactions.filter(interaction_datetime__range=[start_date, end_date])
    interaction_serializer = SafeInteractionSerializer(interactions, many = True)
    if len(interaction_serializer.data) == 0:
        return Response(interaction_serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(interaction_serializer.data, status.HTTP_200_OK)

def get_interaction_list_by_id(id, request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if request.path.split("?")[0] == f'/interaction/get-zone-list/{id}':
        interactions = Interaction.objects.filter(service__zone_id=id)
    elif request.path.split("?")[0] == f'/interaction/get-service-list/{id}':
        interactions = Interaction.objects.filter(service_id=id)
    if start_date and end_date:
        interactions = interactions.filter(interaction_datetime__range=[start_date, end_date])
    interaction_serializer = SafeInteractionSerializer(interactions, many = True)
    if len(interaction_serializer.data) == 0:
        return Response(interaction_serializer.data, status.HTTP_204_NO_CONTENT)
    return Response(interaction_serializer.data, status.HTTP_200_OK)

# def get_interaction_full_list(request):
#     organization_id = request.service.organization_id
#     interactions = Interaction.objects.filter(organization_id=organization_id)
#     interaction_serializer = InteractionSerializer(interactions, many = True)
#     if len(interaction_serializer.data) == 0:
#         return Response(interaction_serializer.data, status.HTTP_204_NO_CONTENT)
#     return Response(interaction_serializer.data, status.HTTP_200_OK)

# def get_interaction_user_list(request):
#     customuser_id = request.user.id
#     interactions = Interaction.objects.filter(customuser_id=customuser_id)
#     interaction_serializer = InteractionSerializer(interactions, many = True)
#     if len(interaction_serializer.data) == 0:
#         return Response(interaction_serializer.data, status.HTTP_204_NO_CONTENT)
#     return Response(interaction_serializer.data, status.HTTP_200_OK)

def create_interaction(data):
    try:
        customuser = CustomUser.objects.get(pk=data['customuser_id'])
        service = Service.objects.get(pk=data['service_id'])
        if customuser.organization_id != service.organization_id:
            return Response({'message': "User can create interactions only in his/her organization"}, status.HTTP_403_FORBIDDEN)
        serializer = InteractionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
