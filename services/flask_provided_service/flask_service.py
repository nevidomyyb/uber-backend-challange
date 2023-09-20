from services.core import EmailService
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_smorest import abort
import os
from log import registerLog
class FlaskProvidedEmailService(EmailService):
    def __init__(self):
        self.smtp_server = os.environ.get("MAIL_SERVER")
        self.smtp_username = os.environ.get("MAIL_USER")
        self.smtp_port = int(os.environ.get("MAIL_PORT"))
        self.smtp_password = os.environ.get("MAIL_PASSWORD")
        self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)

    def initialize_server(self):
        try:
            self.server.starttls()
            self.server.login(self.smtp_username, self.smtp_password)
            
        except Exception as e:
            abort(500, message='An error occured while initializing smtp server')
    @staticmethod
    def create_msg(to, subject, body, username):
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))
        msg['From'] = username
        msg['To'] = to
        msg['Subject'] = subject
        return msg

    @classmethod
    def check_avaliability(cls):
        smtp_server = os.environ.get("MAIL_SERVER")
        smtp_username = os.environ.get("MAIL_USER")
        smtp_port = int(os.environ.get("MAIL_PORT"))
        smtp_password = os.environ.get("MAIL_PASSWORD")
        try:
            client = smtplib.SMTP(
                smtp_server, smtp_port
            )
            client.starttls()
            client.login(smtp_username, smtp_password)
            return True
        except Exception as e:
            return False

    def send_email(self, to, subject, body):
        self.initialize_server()
        msg = self.create_msg(to, subject, body, self.smtp_username)
        try:
            self.server.sendmail(
                self.smtp_username,
                to,
                msg.as_string()
            )
            registerLog('log.txt', 'system', 'Email sent using flask')
            return {'message': "Email sent", 'code': 200}
        except Exception as e:
            return {'message': 'Error during sending email', 'code': 500, 'error': str(e)}
        
