# myapp/urls.py

from django.urls import path
from ..views.views import CommentCreateView, CommentLikeCreateView, FriendsPostList, PostCreateView, PostLikeCreateView, UserCreateView, UserList, PostList, CommentListByPostID

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('comments/<int:post_id>/', CommentListByPostID.as_view(), name='comment-list-by-post-id'),
    path('friends/posts/<int:user_id>/', FriendsPostList.as_view(), name='friends-post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/like/', PostLikeCreateView.as_view(), name='post-like-create'),
    path('comments/<int:comment_id>/like/', CommentLikeCreateView.as_view(), name='comment-like-create'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]
