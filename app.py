import os
from flask import Flask
from flask_smorest import Api

from resources.aws_email_sender import blp as EmailSenderAWSBlueprint
from resources.router_email_sender import blp as EmailRouterBlueprint
from resources.flask_email_sender import blp as EmailSenderFlaskBlueprint

from log import createArchive, checkArchiveExistence

def create_app():
    app = Flask(__name__, instance_path=os.getcwd())

    app.config["PROPAGATION_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Email Service Api"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    api.register_blueprint(EmailSenderAWSBlueprint)
    api.register_blueprint(EmailSenderFlaskBlueprint)
    api.register_blueprint(EmailRouterBlueprint)

    exist = checkArchiveExistence("log.txt")
    if not exist:
        createArchive('log.txt')

    return app