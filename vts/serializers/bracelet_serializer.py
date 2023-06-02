from rest_framework import serializers
from ..models import Bracelet, CustomUser, Organization

class BraceletSerializer(serializers.Serializer):
    rfid = serializers.CharField(max_length=100)
    status = serializers.BooleanField()
    activation_date = serializers.DateField()
    deactivation_date = serializers.DateField()
    customuser_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), 
        allow_null=True, 
        required=False)
    organization_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), source='organization')

    def create(self, validated_data):
        return Bracelet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rfid = validated_data.get('rfid', instance.rfid)
        instance.status = validated_data.get('status', instance.status)
        instance.activation_date = validated_data.get('activation_date', instance.activation_date)
        instance.deactivation_date = validated_data.get('deactivation_date', instance.deactivation_date)
        instance.customuser_id = validated_data.get('customuser_id', instance.customuser_id)
        instance.organization_id = validated_data.get('organization_id', instance.organization_id)
        instance.save()
        return instance