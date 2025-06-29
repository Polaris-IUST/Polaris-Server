from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

from .serializers import (
    UserSerializer, MapDataSerializer, DNSDataSerializer, HTTPResponseSerializer,
    SMSTestSerializer, PingTestSerializer, DownloadTestSerializer,
    UploadTestSerializer, MeasuredLatencySerializer
)
from .models import (
    MapData, DNSData, HTTPResponse, SMSTest, PingTest,
    DownloadTest, UploadTest, MeasuredLatency
)

User = get_user_model()


class SignupView(APIView):
    """
    POST /signup/
    Creates a new user account.
    """
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseDataCreateView(APIView):
    """
    Base view for creating data entries associated with the authenticated user.
    Subclasses must define:
    - serializer_class
    - model_class (optional for further customization)
    """
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


# ------- MapData Views -------
class MapDataCreateView(BaseDataCreateView):
    serializer_class = MapDataSerializer
    permission_classes = [IsAuthenticated]
    model_class = MapData


class MapDataListView(generics.ListAPIView):
    """
    GET /mapdata/
    Returns all MapData entries of the authenticated user.
    """
    serializer_class = MapDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MapData.objects.filter(client=self.request.user)


# ------- DNSData Views -------
class DNSDataCreateView(BaseDataCreateView):
    serializer_class = DNSDataSerializer
    permission_classes = [IsAuthenticated]
    model_class = DNSData


class DNSDataListView(generics.ListAPIView):
    serializer_class = DNSDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DNSData.objects.filter(client=self.request.user)


# ------- HTTPResponse Views -------
class HTTPResponseCreateView(BaseDataCreateView):
    serializer_class = HTTPResponseSerializer
    permission_classes = [IsAuthenticated]
    model_class = HTTPResponse


class HTTPResponseListView(generics.ListAPIView):
    serializer_class = HTTPResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HTTPResponse.objects.filter(client=self.request.user)


# ------- SMSTest Views -------
class SMSTestCreateView(BaseDataCreateView):
    serializer_class = SMSTestSerializer
    permission_classes = [IsAuthenticated]
    model_class = SMSTest


class SMSTestListView(generics.ListAPIView):
    serializer_class = SMSTestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SMSTest.objects.filter(client=self.request.user)


# ------- PingTest Views -------
class PingTestCreateView(BaseDataCreateView):
    serializer_class = PingTestSerializer
    permission_classes = [IsAuthenticated]
    model_class = PingTest


class PingTestListView(generics.ListAPIView):
    serializer_class = PingTestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PingTest.objects.filter(client=self.request.user)


# ------- DownloadTest Views -------
class DownloadTestCreateView(BaseDataCreateView):
    serializer_class = DownloadTestSerializer
    permission_classes = [IsAuthenticated]
    model_class = DownloadTest


class DownloadTestListView(generics.ListAPIView):
    serializer_class = DownloadTestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DownloadTest.objects.filter(client=self.request.user)


# ------- UploadTest Views -------
class UploadTestCreateView(BaseDataCreateView):
    serializer_class = UploadTestSerializer
    permission_classes = [IsAuthenticated]
    model_class = UploadTest


class UploadTestListView(generics.ListAPIView):
    serializer_class = UploadTestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UploadTest.objects.filter(client=self.request.user)


# ------- MeasuredLatency Views -------
class MeasuredLatencyCreateView(BaseDataCreateView):
    serializer_class = MeasuredLatencySerializer
    permission_classes = [IsAuthenticated]
    model_class = MeasuredLatency


class MeasuredLatencyListView(generics.ListAPIView):
    serializer_class = MeasuredLatencySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MeasuredLatency.objects.filter(client=self.request.user)
