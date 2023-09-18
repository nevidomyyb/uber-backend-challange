from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.email_schema import EmailSchema
from services.check_services import CheckService
from services.flask_provided_service.flask_service import FlaskProvidedEmailService
from services.aws_ses_service.ses_service import AWSSESEmailService
from flask import jsonify

blp = Blueprint("email_router", __name__, description='Email sender')

@blp.route('/api/send_mail/')
class EmailSender(MethodView):

    @blp.arguments(EmailSchema)
    @blp.response(200, EmailSchema)
    def post(self, email_data):
        services_avaliable = CheckService.check_services()
        if services_avaliable["avaliable"] == False:
            abort(500, message="No services avaliable")
        for key, value in services_avaliable.items():
            if key != "avaliable":
                if key == "flask_service" and value == True:
                    service = FlaskProvidedEmailService()
                    response = service.send_email(
                        **email_data
                    )
                    return jsonify({**response})
                if key == "aws_service" and value == True:
                    service = AWSSESEmailService(region_name='sa-east-1')
                    response = service.send_email(**email_data)
                    return jsonify({**response})