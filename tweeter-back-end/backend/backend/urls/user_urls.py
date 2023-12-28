# urls/user_urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from views.user_view import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls