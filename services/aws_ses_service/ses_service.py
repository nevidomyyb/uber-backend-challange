import boto3
from services.core import EmailService


#Utilizando a interface do EmailService para implementar a funcionalidade do serviço da SES da Amazon.
class AWSSESEmailService(EmailService):
    
    def __init__(self, region_name):
        self.region_name = region_name
        self.ses = boto3.client('ses', region_name=self.region_name)
    
    @classmethod    
    def check_avaliability(cls, region_name):
        client = boto3.client('ses', region_name=region_name)
        try:
            response = client.get_send_quota()
            return True
        except Exception as e:
            return False


    def send_email(self, to, subject, body):
        try:
            response = self.ses.send_email(
                Source="idk.pedroc@gmail.com",
                Destination={
                    "ToAddresses": [to, ]
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
            print(e)
            return {'message': 'Error during sending email', 'code': 500, 'error': str(e)}
        