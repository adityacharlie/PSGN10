from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from .serializers import LoginSerializer, CustomerSerializer
from .models import Customer


class UserInfo(RetrieveAPIView):
    """ get user infos """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = None
    permission_classes = IsAuthenticated,

    def get_object(self):
        return self.request.user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_type(request):
    """ return the type of the user """
    return Response({
        'user_type': request.user.get_user_type(),
    })


class Login(APIView):
    """ post email/password """
    authentication_classes = (SessionAuthentication,)
    permission_classes = AllowAny,

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if not user or not user.is_active:
            return HttpResponseBadRequest(
                content='Could not login user'
            )
        login(request, user)
        return Response(CustomerSerializer(request.user).data)


class Logout(APIView):
    """ logout on GET """
    permission_classes = AllowAny,

    def get(self, request):
        logout(request)
        return Response({
            'message': 'user logout',
        })

