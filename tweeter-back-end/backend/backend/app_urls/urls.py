# myapp/urls.py

from django.urls import path
from ..views.views import UserList, PostList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('posts/', PostList.as_view(), name='post-list'),
]
