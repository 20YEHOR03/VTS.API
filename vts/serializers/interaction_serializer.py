from rest_framework import serializers
from ..models.interaction import Interaction
from ..models.customuser import CustomUser
from ..models.service import Service

class InteractionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customuser_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='customuser')
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), source='service')
    interaction_datetime = serializers.DateTimeField()
    info = serializers.CharField(allow_null=True)


    def create(self, validated_data):
        return Interaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customuser = validated_data.get('customuser', instance.customuser)
        instance.service = validated_data.get('service', instance.service)
        instance.interaction_datetime = validated_data.get('interaction_datetime', instance.interaction_datetime)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance
    
class SafeInteractionSerializer(serializers.Serializer):
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), source='service')
    interaction_datetime = serializers.DateTimeField()
    info = serializers.CharField(allow_null=True)