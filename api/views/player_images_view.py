from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import PlayerImages
from ..serializers import PlayerImagesSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerImageViewSet(viewsets.ModelViewSet):
    queryset = PlayerImages.objects.all()
    serializer_class = PlayerImagesSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerImageView(viewsets.ViewSet):
    def get_id(self, username):
        try:
            user = User.objects.get(username=username)
            return user.id
        except User.DoesNotExist:
            return None

    def retrieve(self, request, username=None):
        """
        Date should be the date from which we want to get the images
        """
        try:
            user_id = self.get_id(username)
            if user_id is None:
                return Response(data={"detail": "Not found"},  status=404)

            date = request.query_params.get("date", None)

            if date is not None:
                images = PlayerImages.objects.filter(user=user_id, date__gte=date)
            else:
                images = PlayerImages.objects.filter(user=user_id)  # Get all images

            serializer = PlayerImagesSerializer(images, many=True)

            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(None)
