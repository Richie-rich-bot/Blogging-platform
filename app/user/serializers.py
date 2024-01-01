from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects"""
    class Meta:
        model = get_user_model()
        fields = ['name','email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}