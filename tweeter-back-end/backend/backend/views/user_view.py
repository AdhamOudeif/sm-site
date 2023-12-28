# views/user_view.py

from rest_framework import viewsets

from models.user_model import User
from serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
