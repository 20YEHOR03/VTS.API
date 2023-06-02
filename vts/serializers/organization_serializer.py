from rest_framework import serializers
from ..models.organization import Organization

class OrganizationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance