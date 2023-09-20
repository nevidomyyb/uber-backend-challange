import unittest
from app import create_app

class SMTPLibTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_avaliability_smtplib_service(self):
        response = self.client.get('/api/check_services/')
        response = response.get_json()
        self.assertEqual(True, response["flask_service"])

    def test_smtplib_send_mail(self):
        json = {
            "subject": "E-mail teste",
            "body": "esse é um email teste",
            "to": "idk.pedroc@gmail.com"
        }
        response = self.client.post('/api/send_mail/flask/', json=json)
        response = response.get_json()
        self.assertEqual(200, response["code"])