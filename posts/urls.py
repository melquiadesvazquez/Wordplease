from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet
from posts.views import HomeView, UserPostsView, PostDetailView, NewPostView

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('blogs/<slug:username>', UserPostsView.as_view(), name='user_posts'),
    path('blogs/<slug:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('blogs/new', NewPostView.as_view(), name='new_post'),
    path('', HomeView.as_view(), name='home'),

    # API
    path('api/1.0/', include(router.urls)),
]