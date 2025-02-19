from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import FriendshipSerializer
from ..models import Friendship, Chat


from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class FriendshipViewSet(viewsets.ViewSet):
    def get_id(self, username):
        try:
            user = User.objects.get(username=username)
            return user.id
        except User.DoesNotExist:
            Response({'message': 'user does not existtt'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request):
        try:
            user_id = request.user.id
            username = request.user.username

            friendship = Friendship.objects.filter(user1=user_id) | Friendship.objects.filter(user2=user_id)
            serializer = FriendshipSerializer(friendship, many=True, context={'username': username})
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)

    def create(self, request):
        data = request.data
        if 'user' not in data:
            return Response({'message': 'user not provided'}, status=status.HTTP_400_BAD_REQUEST)
        user2 = User.objects.get(username=data['user'])

        user = request.user
        try:
            Friendship.objects.create(
                user1=user,
                user2=user2,
            )
            chat = Chat.objects.get(user1=user, user2=user2)
            return Response({'chat_id': chat.id}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'message': 'the friendship already exists'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data
        if 'user' not in data:
            return Response({'message': 'user not provided'}, status=status.HTTP_400_BAD_REQUEST)
        username = data['user']
        user2 = self.get_id(username)
        user = request.user
        user1 = self.get_id(user.username)

        try:
            friendship = (Friendship.objects.filter(user1=user1, user2=user2)
                          | Friendship.objects.filter(user1=user2, user2=user1))
            friendship.delete()
        except Friendship.DoesNotExist:
            return Response({'message': 'friendship does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)
