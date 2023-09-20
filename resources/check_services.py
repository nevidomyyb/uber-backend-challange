from flask.views import MethodView
from flask_smorest import Blueprint, abort
from services.check_services import CheckService
from flask import jsonify

blp = Blueprint("check_services", __name__, description='Email sender')

@blp.route('/api/check_services/')
class CheckServices(MethodView):

    @blp.response(200)
    def get(self):
        services_avaliable = CheckService.check_services()
       
        return jsonify({**services_avaliable})