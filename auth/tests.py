import json
from django.test import TestCase,Client
from rest_framework import status

client = Client()

class AuthTest(TestCase):
    def setUp(self):
        self.payload_valid = {
            "username": "han_solo",
            "password": "senha1234",
            "password_confirm": "senha1234"
        }
        self.payload_invalid = {
            "username": "darth_vader",
            "password": "senha1234",
            "password_confirm": "senha"
        }
    def test_create_user(self):
        response = client.post(
            '/api-register/',
            content_type='application/json',
            data=json.dumps(self.payload_valid),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_user_invalid(self):
        response = client.post(
            '/api-register/',
            content_type='application/json',
            data=json.dumps(self.payload_invalid),
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)