from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'username', 'password']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']