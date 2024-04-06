# myapp/models.py

from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.EmailField()
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Birthdate = models.DateField()
    Gender = models.CharField(max_length=10)
    ProfilePicture = models.CharField(max_length=255)
    RegistrationDate = models.DateTimeField()
    class Meta:
        app_label = 'backend'
        db_table = 'user'

class Post(models.Model):
    PostID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='UserID')
    Content = models.TextField()
    Photo = models.CharField(max_length=255, blank=True, null=True)
    Timestamp = models.DateTimeField()
    LikesCount = models.IntegerField(default=0)
    CommentsCount = models.IntegerField(default=0)
    SharesCount = models.IntegerField(default=0)
    class Meta:
        app_label = 'backend'
        db_table = 'post'        

class Comment(models.Model):
    CommentId = models.AutoField(primary_key=True)
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='PostID')
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='UserID')
    Content = models.TextField()
    Timestamp = models.DateTimeField()
    LikesCount = models.IntegerField(default=0)
    class Meta:
        app_label = 'backend'
        db_table = 'comment'    

class Friendship(models.Model):
    FriendshipID = models.AutoField(primary_key=True)
    User1ID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='User1ID', related_name='friends1')
    User2ID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='User2ID', related_name='friends2')
    Status = models.CharField(max_length=20)

    class Meta:
        app_label = 'backend'
        db_table = 'friendship'    
