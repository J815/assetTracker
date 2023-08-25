from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceLog,DeviceType
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer,DeviceTypeSerializer

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserRegistrationSerializer

from .payments import create_subscription

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    authentication_classes = [] 
    permission_classes=[]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



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


class LogoutView(APIView):
    def post(self, request):
        token = Token.objects.get(user=request.user)
        # Delete the token
        token.delete()
        
        return Response({"message":" you are logged out"},status=status.HTTP_200_OK)


# for subscription
class SubscriptionPurchaseView(APIView):
    def post(self, request, *args, **kwargs):
        
        data = request.data
        user_id = data.get('user_id')
        subscription_plan = data.get('subscription_plan')

        if user_id and subscription_plan:
            subscription=create_subscription(subscription_plan,user_id)
            return Response({'message': f'Subscription plan "{subscription.plan}" purchased for user {subscription.id}'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid data provided'},
                            status=status.HTTP_400_BAD_REQUEST)





