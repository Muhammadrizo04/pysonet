from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserPublicSerializer


class UserNetPublicView(ModelViewSet):
    """displaying public user profile"""

    queryset = UserNet.objects.all()
    serializer_class = GetUserPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(ModelViewSet):
    """user profile output"""

    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
