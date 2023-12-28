# backend/models/post_model.py
from django.db import models
from .user_model import User  # Import the User model if it's in the same app

class Post(models.Model):
    PostID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.TextField()
    Photo = models.CharField(max_length=255)
    Timestamp = models.DateTimeField(auto_now_add=True)
    LikesCount = models.IntegerField(default=0)
    CommentsCount = models.IntegerField(default=0)
    SharesCount = models.IntegerField(default=0)
