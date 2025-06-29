from django.urls import path

from .views import (
    SignupView, MapDataView, DNSDataView, HTTPResponseView,
    SMSTestView, PingTestView, DownloadTestView,
    UploadTestView, MeasuredLatencyView
)

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('mapdata/', MapDataView.as_view()),
    path('dns/', DNSDataView.as_view()),
    path('http/', HTTPResponseView.as_view()),
    path('sms/', SMSTestView.as_view()),
    path('ping/', PingTestView.as_view()),
    path('download/', DownloadTestView.as_view()),
    path('upload/', UploadTestView.as_view()),
    path('latency/', MeasuredLatencyView.as_view()),
]
