from datetime import datetime

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
            username = request.query_params.get('username')
            if username is None:
                user_id = request.user.id
                username = request.user.username
            else:
                user_id = self.get_id(username)

            friendship = Friendship.objects.filter(user1=user_id) | Friendship.objects.filter(user2=user_id)
            serializer = FriendshipSerializer(friendship, many=True, context={'username': username})
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)

    def create(self, request):
        data = request.data
        user = request.user
        try:
            Friendship.objects.create(
                user1=user,
                user2=User.objects.get(username=data['user']),
                date=datetime.now()
            )
            chat = Chat.objects.create(
                user1=user,
                user2=User.objects.get(username=data['user'])
            )
            return Response({'chat_id': chat.id}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'message', 'the friendship already exists'}, status=status.HTTP_400_BAD_REQUEST)
