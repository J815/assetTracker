from django.shortcuts import render

from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceLog,DeviceType
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer,DeviceTypeSerializer

# for Company view
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# for employee view
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# for  device type view
class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer


# for  device view
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# for  devicelog view
class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
