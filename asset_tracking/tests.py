# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Company, Employee

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# test for employee model and view

    
        
class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')