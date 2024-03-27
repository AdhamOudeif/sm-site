# myapp/urls.py

from django.urls import path
from ..views.views import UserList, PostList, CommentListByPostID

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('comments/<int:post_id>/', CommentListByPostID.as_view(), name='comment-list-by-post-id'),
]
