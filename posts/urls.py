from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet
from posts.views import PostDetailView, BlogPostsView, BlogsView, NewPostView, HomeView

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('blogs/<slug:blog_slug>/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blogs/<slug:blog_slug>/', BlogPostsView.as_view(), name='blog_posts'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('new-post/', NewPostView.as_view(), name='new_post'),
    path('', HomeView.as_view(), name='home'),

    # API
    path('api/1.0/', include(router.urls))
]