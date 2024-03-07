# api/views.py

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


# Example view for Endpoint1
class Endpoint1View(APIView):
    def get(self, request):
        # Example response data
        data = {"message": "This is Endpoint 1"}
        return JsonResponse(data)


# Example view for Endpoint2
class Endpoint2View(APIView):
    def get(self, request):
        # Example response data
        data = {"message": "This is Endpoint 2"}
        return Response(data)
