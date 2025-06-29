from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer, MapDataSerializer, DNSDataSerializer, HTTPResponseSerializer,
    SMSTestSerializer, PingTestSerializer, DownloadTestSerializer,
    UploadTestSerializer, MeasuredLatencySerializer
)

User = get_user_model()


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseDataCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = None
    model_class = None

    def post(self, request):
        data = request.data.copy()
        data['client'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data stored"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MapDataView(BaseDataCreateView):
    serializer_class = MapDataSerializer


class DNSDataView(BaseDataCreateView):
    serializer_class = DNSDataSerializer


class HTTPResponseView(BaseDataCreateView):
    serializer_class = HTTPResponseSerializer


class SMSTestView(BaseDataCreateView):
    serializer_class = SMSTestSerializer


class PingTestView(BaseDataCreateView):
    serializer_class = PingTestSerializer


class DownloadTestView(BaseDataCreateView):
    serializer_class = DownloadTestSerializer


class UploadTestView(BaseDataCreateView):
    serializer_class = UploadTestSerializer


class MeasuredLatencyView(BaseDataCreateView):
    serializer_class = MeasuredLatencySerializer
