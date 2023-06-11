from rest_framework import serializers
from ..models import Gender, Role, Organization

class AccessInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    gender_id = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all(), allow_null=True, source='gender')
    age = serializers.IntegerField(allow_null=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), allow_null=True, source='role')
    organization_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), allow_null=True, source='organization')
    