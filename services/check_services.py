from services.aws_ses_service.ses_service import AWSSESEmailService
from services.flask_provided_service.flask_service import FlaskProvidedEmailService

class CheckService():
    
    def __init__(self):
        super(self).__init__()

    @staticmethod
    def check_aws_service():
        aws_service = AWSSESEmailService
        response = aws_service.check_avaliability(region_name='sa-east-1')
        return response
    @staticmethod
    def check_flask_service():
        flask_service = FlaskProvidedEmailService
        response = flask_service.check_avaliability()
        return response
    @classmethod
    def check_services(cls):
        flask_response = cls.check_flask_service()
        aws_response = cls.check_aws_service()
        response = {
            "flask_service": flask_response,
            "aws_service": aws_response
        }
        response["avaliable"] = True if flask_response or aws_response else False
        return response