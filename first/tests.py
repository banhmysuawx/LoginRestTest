from cgi import test
from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
# Create your tests here.
class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
    
    
    def test_login(self):
        data = {
            "username": "test",
            "password": "test"
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, 200)
        
        
    def test_login_fail(self):
        data = {
            "username": "test",
            "password": "test1"
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, 401)
        
    
    def test_login_fail_2(self):
        data = {
            "username": "test1",
            "password": "test"
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, 401)
        