from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)



class MapData(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.CharField(max_length=100)
    distanceWalked = models.FloatField()
    technology = models.CharField(max_length=100)
    nodeId = models.CharField(max_length=100)
    plmnId = models.CharField(max_length=100)
    lac = models.CharField(max_length=100)
    rac = models.CharField(max_length=100, null=True, blank=True)
    tac = models.CharField(max_length=100)
    cellId = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    arfcan = models.IntegerField(null=True, blank=True)
    signalStrength = models.IntegerField()
    scanTech = models.CharField(max_length=100)
    signalQuality = models.IntegerField()
    scanServingSigPow = models.IntegerField()


class DNSData(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    responsetime = models.FloatField()
    hostname = models.CharField(max_length=255)
    time = models.DateTimeField()


class HTTPResponse(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    responsetime = models.FloatField()
    hostname = models.CharField(max_length=255)
    time = models.DateTimeField()


class SMSTest(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    deliveryTime = models.FloatField()
    phoneNumber = models.CharField(max_length=50)
    time = models.DateTimeField()


class PingTest(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    avgResponseTime = models.FloatField()
    suceessCountRate = models.FloatField()
    hostname=models.CharField(255, default="google.com")
    time = models.DateTimeField()


class DownloadTest(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    DownloadSpeed = models.FloatField()
    Duration = models.CharField(max_length=100)
    time = models.DateTimeField()


class UploadTest(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    UploadSpeed = models.FloatField()
    Duration = models.FloatField()
    time = models.DateTimeField()


class MeasuredLatency(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    avgLatency = models.FloatField()
    jitter = models.FloatField()
    time = models.DateTimeField()
