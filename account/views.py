from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import UserRegisterSerializer

User = get_user_model()


class UserRegistration(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
