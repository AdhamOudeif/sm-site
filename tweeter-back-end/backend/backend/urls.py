# Urls

from django.contrib import admin
from django.urls import path, include
from backend.urls.user_urls import urlpatterns as user_urls
from backend.urls.post_urls import urlpatterns as post_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(user_urls)),
    path('api/posts/', include(post_urls)),
]
