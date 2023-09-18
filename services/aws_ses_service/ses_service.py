import boto3
from services.core import EmailService

class AWSSESEmailService(EmailService):
    
    def __init__(self, region_name):
        self.region_name = region_name
        self.ses = boto3.client('ses', region_name=self.region_name)

    def send_email(self, to, subject, body):
        try:
            response = self.ses.send_email(
                Source="idk.pedroc@gmail.com",
                Destination={
                    "ToAddress": [to]
                },
                Message={
                    "Subject": {
                        "Data": subject
                    },
                    "Body": {
                        "Text": {
                            "Data": body
                        }
                    }
                }
            )
            return {'message': "Email sent", 'code': 200}
        except Exception as e:
            return {'message': 'Error during sending email', 'code': 500, 'error': str(e)}
        