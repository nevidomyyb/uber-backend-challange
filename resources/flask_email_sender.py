from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort
from services.flask_provided_service.flask_service import FlaskProvidedEmailService
from schemas.email_schema import EmailSchema

blp = Blueprint("emailflask", __name__, description='Email sender')

@blp.route('/api/send_mail/flask/')
class EmailSender(MethodView):
    @blp.arguments(EmailSchema)
    @blp.response(200, EmailSchema)
    def post(self, email_data):
        EmailService = FlaskProvidedEmailService()
        response =EmailService.send_email(
            to=email_data["to"],
            subject=email_data["subject"],
            body=email_data["subject"]
        )
        if response["code"] == 200:
            return jsonify({"code": 200, "message": "Email sent"})
        else:
            abort(500, message="An error occured while sending email")