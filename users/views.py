from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import (
    UserSerializer,
    ProfileSerializer,
    UserProfileSerializer,
)

from users.models import (
    Profile
)

from django.contrib.auth.models import User

from django.forms.models import model_to_dict


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_serializer = UserProfileSerializer(user)
        token['user'] = user_serializer.data
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserProfileSerializer
        return UserSerializer


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )

    def partial_update(self, request, *args, **kwargs):
        response = super(ProfileViewSet, self).partial_update(request, *args, **kwargs)
        perfil_updated = Profile.objects.get(pk=request.data['id'])
        perfil_updated.save()
        perfil_updated.user.set_password(perfil_updated.raw_password)
        perfil_updated.user.save()
        return response
