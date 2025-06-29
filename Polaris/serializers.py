from rest_framework import serializers
from django.contrib.auth import get_user_model
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
