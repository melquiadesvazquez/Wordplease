from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs.api import BlogViewSet
from blogs.views import BlogListView, NewBlogView, BlogDetailView
from categories.api import CategoryViewSet
from categories.views import CategoryListView, CategoryDetailView, NewCategoryView
from posts.api import PostViewSet
from posts.views import PostListView, PostDetailView, NewPostView
from users.api import UserViewSet
from users.views import UserListView, UserDetailView, NewUserView, LoginView, LogoutView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('blogs', BlogViewSet)
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Users
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('signup/', NewUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Blogs
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new-blog/', NewBlogView.as_view(), name='new_blog'),

    # Categories
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('new-category/', NewCategoryView.as_view(), name='new_category'),

    # Posts
    path('blogs/<slug:blog_slug>/', PostListView.as_view(), name='post_list'),
    path('blogs/<slug:blog_slug>/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new-post/', NewPostView.as_view(), name='new_post'),

    # Home
    path('', PostListView.as_view(), name='home'),

    # API
    path('api/v1/', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
