# myapp/views.py

from rest_framework import generics
from ..models.models import User, Post
from ..serializers.serializers import UserSerializer, PostSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
