from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import LoginSerializer, CustomerSerializer


class Login(APIView):
    """ post email/password """
    authentication_classes = (SessionAuthentication,)
    permission_classes = AllowAny,

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(request, email=email, password=password)
        if not user or not user.is_active:
            return HttpResponseBadRequest(
                content='Could not login user'
            )
        login(request, user)
        return Response(CustomerSerializer(request.user).data)
