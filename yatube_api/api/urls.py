from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

# Роутеры для автоматической маршрутизации API
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='followers')
router.register(r'^posts/(?P<post_pk>\d+)/comments', CommentViewSet,
                basename='comments'
                )

# Паттерны URL для API и аутентификации
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
