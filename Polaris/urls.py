from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    SignupView,

    MapDataCreateView, MapDataListView,
    DNSDataCreateView, DNSDataListView,
    HTTPResponseCreateView, HTTPResponseListView,
    SMSTestCreateView, SMSTestListView,
    PingTestCreateView, PingTestListView,
    DownloadTestCreateView, DownloadTestListView,
    UploadTestCreateView, UploadTestListView,
    MeasuredLatencyCreateView, MeasuredLatencyListView,
)

urlpatterns = [
    # Get access token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('signup/', SignupView.as_view(), name='signup'),

    # MapData
    path('mapdata/create/', MapDataCreateView.as_view(), name='mapdata-create'),
    path('mapdata/', MapDataListView.as_view(), name='mapdata-list'),

    # DNSData
    path('dnsdata/create/', DNSDataCreateView.as_view(), name='dnsdata-create'),
    path('dnsdata/', DNSDataListView.as_view(), name='dnsdata-list'),

    # HTTPResponse
    path('httpresponse/create/', HTTPResponseCreateView.as_view(), name='httpresponse-create'),
    path('httpresponse/', HTTPResponseListView.as_view(), name='httpresponse-list'),

    # SMSTest
    path('smstest/create/', SMSTestCreateView.as_view(), name='smstest-create'),
    path('smstest/', SMSTestListView.as_view(), name='smstest-list'),

    # PingTest
    path('pingtest/create/', PingTestCreateView.as_view(), name='pingtest-create'),
    path('pingtest/', PingTestListView.as_view(), name='pingtest-list'),

    # DownloadTest
    path('downloadtest/create/', DownloadTestCreateView.as_view(), name='downloadtest-create'),
    path('downloadtest/', DownloadTestListView.as_view(), name='downloadtest-list'),

    # UploadTest
    path('uploadtest/create/', UploadTestCreateView.as_view(), name='uploadtest-create'),
    path('uploadtest/', UploadTestListView.as_view(), name='uploadtest-list'),

    # MeasuredLatency
    path('measuredlatency/create/', MeasuredLatencyCreateView.as_view(), name='measuredlatency-create'),
    path('measuredlatency/', MeasuredLatencyListView.as_view(), name='measuredlatency-list'),
]
