from __future__ import division

import datetime

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from api.models import *

class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        update_last_login(None, validated_data["user"])
        return validated_data

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "account_type", "password")


class UserSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    def get_students(self, obj):
        students = Student.objects.filter(sponsor=obj)
        return StudentSeriaizer(students, many=True).data

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep.pop("password", None)
        return rep

    class Meta:
        model = User
        fields = "__all__"
        write_only_fields = ("password",)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=120)
    new_password = serializers.CharField(max_length=120)

class StudentTypeSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = StudentType
        fields = "__all__"

class StudentSeriaizer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super(StudentSeriaizer, self).to_representation(instance)
        rep["student_type"] = StudentTypeSeriaizer(instance.student_type).data
        return rep

    class Meta:
        model = Student
        fields = "__all__"
        # getting the student_type object rather than just returning the ID
        extra_kwargs = {
            "student_type": {
                "default": serializers.CreateOnlyDefault(
                    serializers.CurrentUserDefault()
                )
            }
        }






