from rest_framework import serializers
from ..models import Service, Gender, Organization, Role, Zone

class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_null=True)
    minimum_age = serializers.IntegerField(default=0)
    organization_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), source='organization')
    zone_id = serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all(), allow_null=True, source='zone')
    allowed_genders = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all(), many=True)
    allowed_roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    def create(self, validated_data):
        allowed_genders_data = validated_data.pop('allowed_genders', [])
        allowed_roles_data = validated_data.pop('allowed_roles', [])
        service = Service.objects.create(**validated_data)
        service.allowed_genders.set(allowed_genders_data)
        service.allowed_roles.set(allowed_roles_data)
        return service

    def update(self, instance, validated_data):
        print(validated_data)
        allowed_genders_data = [gender.id for gender in validated_data.pop('allowed_genders', [])]
        allowed_roles_data = [role.id for role in validated_data.pop('allowed_roles', [])]
        instance.organization_id = validated_data.get('organization', instance.organization_id)
        print(instance.zone_id)
        instance.zone_id = validated_data.get('zone', instance.zone_id)
        print(instance.zone_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.minimum_age = validated_data.get('minimum_age', instance.minimum_age)
        instance.save()
        instance.allowed_genders.set(allowed_genders_data)
        instance.allowed_roles.set(allowed_roles_data)
        return instance
