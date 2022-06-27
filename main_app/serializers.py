from rest_framework import serializers
from .models import SystemUser


class systemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields =("slugId",
                "firstName",
                "lastName",
                "userName",
                "passWord",
                "confirmPass",
                "email",
                "date",)
