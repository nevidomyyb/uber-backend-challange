from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort
from services.aws_ses_service.ses_service import AWSSESEmailService
from schemas.email_schema import EmailSchema

blp = Blueprint("emailaws", __name__, description='Email sender')

@blp.route('/api/send_mail/aws/')
class EmailSender(MethodView):
    @blp.arguments(EmailSchema)
    @blp.response(200, EmailSchema)
    def post(self, email_data):
        EmailService = AWSSESEmailService(region_name='sa-east-1')
        response =EmailService.send_email(
            to=email_data["to"],
            subject=email_data["subject"],
            body=email_data["subject"]
        )
        if response["code"] == 200:
            return jsonify({"code": 200, "message": "Email sent"})
        else:
            abort(500, message="An error occured while sending email")