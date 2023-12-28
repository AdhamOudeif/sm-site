# urls/post_urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from views.post_view import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
urlpatterns = router.urls
