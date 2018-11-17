from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import UsersViewSet
from users.views import LoginView, LogoutView, SignupView, UsersView

router = DefaultRouter()
router.register('users', UsersViewSet, base_name='users')


urlpatterns = [
    path('blogs', UsersView.as_view(), name='blogs'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='register'),

    # API
    path('api/1.0/', include(router.urls))
]
