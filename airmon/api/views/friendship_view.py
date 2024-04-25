from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import FriendshipSerializer
from ..models import Friendship

from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class FriendshipViewSet(viewsets.ViewSet):
    def get_id(self, username):
        user = User.objects.get(username=username)
        return user.id

    def retrieve(self, request, username=None):
        try:
            user_id = self.get_id(username)
            friendship = Friendship.objects.filter(user1=user_id) | Friendship.objects.filter(user2=user_id)
            serializer = FriendshipSerializer(friendship, many=True, context={'username': username})
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(None)
