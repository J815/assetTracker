from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog,DeviceType
from django.contrib.auth.models import User




class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# for company model
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# for employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# for devicetype model
class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'

# for device model
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

# for devicelog model
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'

    def validate(self, data):
        if data['return_date'] and data['return_date'] < data['checkout_date']:
            raise serializers.ValidationError("Return date cannot be earlier than checkout date.")
        return data