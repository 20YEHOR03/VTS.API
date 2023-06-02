from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models.organization import Organization
from ..models.customuser import CustomUser
from ..models.gender import Gender
from ..models.role import Role

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    gender_id = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all(), allow_null=True, source='gender')
    age = serializers.IntegerField(allow_null=True)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), allow_null=True, source='role')
    organization_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), allow_null=True, source='organization')

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender_id = validated_data.get('gender_id', instance.gender_id)
        instance.age = validated_data.get('age', instance.age)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.role_id = validated_data.get('role_id', instance.role_id)
        instance.organization_id = validated_data.get('organization_id', instance.organization_id)
        instance.save()
        return instance

class SafeCustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    gender_id = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all(), allow_null=True, source='gender')
    age = serializers.IntegerField(allow_null=True)