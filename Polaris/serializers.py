from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import (
    MapData, DNSData, HTTPResponse, SMSTest, PingTest,
    DownloadTest, UploadTest, MeasuredLatency
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class EmailAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to find user by email
            try:
                user = User.objects.get(email=email)
                username = user.username
            except User.DoesNotExist:
                raise serializers.ValidationError(_('Invalid email or password.'))

            # Authenticate using username & password
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError(_('Invalid email or password.'))
        else:
            raise serializers.ValidationError(_('Must include "email" and "password".'))

        attrs['user'] = user
        return attrs


class MapDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapData
        fields = '__all__'


class DNSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSData
        fields = '__all__'


class HTTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTTPResponse
        fields = '__all__'


class SMSTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSTest
        fields = '__all__'


class PingTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingTest
        fields = '__all__'


class DownloadTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadTest
        fields = '__all__'


class UploadTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadTest
        fields = '__all__'


class MeasuredLatencySerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasuredLatency
        fields = '__all__'
