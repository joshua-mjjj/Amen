import datetime
import hashlib
import json
import os
import random

from rest_framework import status, serializers
from rest_framework.generics import GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_jwt.views import ObtainJSONWebToken

from rest_auth.registration.serializers import SocialLoginSerializer
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialConnectView, SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from django.core.paginator import Paginator 
from django.http import JsonResponse, HttpResponse 
import xlwt 
from vippu_backend.settings import unique_token

from api.models import *
from api.serializers import *


class AccountLoginAPIView(ObtainJSONWebToken):
    serializer_class = JWTSerializer

class SignUp(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            user.set_password(serializer.validated_data["password"])
            user.save()

            username = serializer.data["username"]

            # Get user by username
            user = User.objects.get(username=username)

            return Response(
                UserSerializer(user, many=False).data, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfile(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # No listing user data
    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # properties 
    @action(detail=True, methods=["GET"])
    def students(self, request, *args, **kwargs):
        user = self.get_object()
        queryset = Student.objects.filter(sponsor=user)
        students = self.paginate_queryset(queryset)
        serializer = StudentSeriaizer(students, many=True)
        return self.get_paginated_response(serializer.data)

class ChangePasswordApi(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data["old_password"]
            new_password = serializer.data["new_password"]

            user = self.request.user

            if not user.check_password(old_password):
                content = {"detail": "Invalid Password"}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.set_password(new_password)
                user.save()
                content = {"success": "Password Changed"}
                return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentTypeList(ListAPIView):
    serializer_class = StudentTypeSeriaizer
    queryset = StudentType.objects.all()

class StudentViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSeriaizer
    queryset = Student.objects.all()

class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
        
