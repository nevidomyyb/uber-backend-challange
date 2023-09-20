import pytest
import unittest
import tracemalloc
from app import create_app

class AWSTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_avaliability_aws_service(self):

        response = self.client.get('/api/check_services/')
        self.assertEqual(True, response.get_json()['aws_service'])

    def test_aws_send_mail(self):

        json = {
            "subject": "E-mail teste",
            "body": "esse é um email teste",
            "to": "idk.pedroc@gmail.com"
        }
        response = self.client.post('/api/send_mail/aws/', json=json)
        self.assertEqual(200, response.get_json()['code'])