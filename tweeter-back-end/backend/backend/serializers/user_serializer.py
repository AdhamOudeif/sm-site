# serializers/user_serializer.py

from rest_framework import serializers
from models.user_model import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
