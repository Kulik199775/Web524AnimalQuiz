from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny

from sections.permissions import IsSuperUser, IsModerator
from users.models import User
from users.user_serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserTokenObtainPairSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsSuperUser | IsModerator)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsSuperUser,)


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    permission_classes = (AllowAny,)