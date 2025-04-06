from django.urls import path
from .views import RegisterView, LoginView
from .views import follow_user, unfollow_user
from .views import UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('users/', UserListView.as_view(), name='user-list'),
]
