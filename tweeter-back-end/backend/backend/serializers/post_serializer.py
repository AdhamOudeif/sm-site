# serializers/post_serializer.py

from rest_framework import serializers
from models.post_model import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
