from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.views import Digest
from .serializers import DigestSerializer


class DigestView(APIView):
    """Обрабатывает запрос от главного приложения"""
    def get(self, request):
        user = request.user
        digest = Digest(user.id)
        serializer = DigestSerializer(digest)
        return Response(serializer.data, status=status.HTTP_200_OK)
