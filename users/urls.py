from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import (UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView,
                         UserTokenObtainPairView)

app_name = UsersConfig.name

urlpatterns = [
    # users urlpatterns
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', never_cache(UserCreateAPIView.as_view()), name='user_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('<int:pk>/update/', never_cache(UserUpdateAPIView.as_view()), name='user_update'),
    path('<int:pk>/delete/', never_cache(UserDestroyAPIView.as_view()), name='user_delete'),

    # token urlpatterns
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
