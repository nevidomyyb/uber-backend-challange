import os
from flask import Flask
from flask_smorest import Api

from resources.email_sender import blp as EmailSenderBlueprint

def create_app():
    app = Flask(__name__, instance_path=os.getcwd())

    app.config["PROPAGATION_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores Rest API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    api.register_blueprint(EmailSenderBlueprint)


    return app