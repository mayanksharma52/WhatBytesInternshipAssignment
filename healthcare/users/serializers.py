from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        name = validated_data.pop('name')
        first_name, *last_name = name.split(' ', 1)
        last_name = last_name[0] if last_name else ''
        validated_data['username'] = validated_data['email']  # Use email as username
        validated_data['first_name'] = first_name
        validated_data['last_name'] = last_name
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)