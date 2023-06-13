from rest_framework import serializers
from ..models import Organization, Zone

class ZoneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_null=True)
    organization_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), source='organization')

    def create(self, validated_data):
        service = Zone.objects.create(**validated_data)
        return service

    def update(self, instance, validated_data):
        instance.organization_id = validated_data.get('organization', instance.organization_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance