from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class FindUserViewSet(viewsets.ViewSet):
    def list(self, request, key=None):
        users = User.objects.filter(username__contains=key)
        limit = 10
        # NO es fa a partir del serializer perque només es retorna el field username
        # serializer = UserSerializer(users, many=True)
        result = []
        for user in users:
            user_obj_serialized = {
                'username': user.username
            }
            result.append(user_obj_serialized)
        return Response(result[:limit])
