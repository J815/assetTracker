from django.db import models
from django.contrib.auth.models import User

# for different companies
class Company(models.Model):
    name = models.CharField(max_length=100)  
    
# employee and the company he works
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class DeviceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.TextField()
    condition_on_return = models.TextField(null=True, blank=True)
