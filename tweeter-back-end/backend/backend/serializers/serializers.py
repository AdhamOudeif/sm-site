# myapp/serializers.py

from rest_framework import serializers
from ..models.models import User, Post, Comment
from django.contrib.auth.hashers import make_password  # Import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FriendsPostList(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('UserID', 'Content', 'Photo')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('UserID', 'PostID', 'Content')

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Username', 'Email', 'Password', 'FirstName', 'LastName', 'Birthdate', 'Gender']
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['Password'] = make_password(validated_data['Password'])
        return User.objects.create(**validated_data)