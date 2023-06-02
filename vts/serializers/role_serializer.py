from rest_framework import serializers
from ..models import Role

class RoleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        role = Role.objects.create(**validated_data)
        return role

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
