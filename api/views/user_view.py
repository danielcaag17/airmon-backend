from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage

from ..models import Player
from ..serializers import UserSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class FindUserViewSet(viewsets.ViewSet):
    def list(self, request, key=None):
        username = request.user.username
        limit = 10
        users = User.objects.filter(username__istartswith=key)[:limit]
        # NO es fa a partir del serializer perque només es retorna el field username
        # serializer = UserSerializer(users, many=True)
        result = []
        for user in users:
            if user.username != username:
                user_obj_serialized = {
                    'username': user.username
                }
                result.append(user_obj_serialized)
        return Response(result)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class EditUserViewSet(viewsets.ViewSet):
    def update(self, request):
        username = request.user.username
        # username = request.data['username']
        data = request.data
        avatar = request.FILES.get('avatar')
        try:
            user = User.objects.get(username=username)
            player = Player.objects.get(user=user)

            if data['password'] != "":
                user.password = data['password']
            user.save()

            if data['language'] != "":
                player.language = data['language']
            if avatar is not None:
                avatar_name = default_storage.save('avatar/' + avatar.name, avatar)
                player.avatar = default_storage.url(avatar_name)
            player.save()

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
