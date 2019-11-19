from flask import Blueprint, request
from app.verification import verification_services
from utils.basic_utils import *


info_extraction_api = Blueprint('info_extraction', __name__)
logo_extraction_api = Blueprint('logo_extraction', __name__)


@info_extraction_api.route("/extraction/info", methods=['POST'])
def info_extraction_handler():
    try:
        if request.is_json:
            response = verification_services.info_extraction_service(request.get_json())
            logger.info('INFO EXTRACTION DONE SUCCESSFULLY')
            return jsonify(response['result'])
        else:
            return jsonify(BAD_INPUT)

    except Exception as ex:
        exception_response(ex)
        return "exception occured", 400


@logo_extraction_api.route("/extraction/logo", methods=['POST'])
def logo_extraction_handler():
    try:
        if request.is_json:
            response = verification_services.logo_extraction_service(request.get_json())
            logger.info('LOGO EXTRACTION DONE SUCCESSFULLY')
            return jsonify(response['result'])
        else:
            return jsonify(BAD_INPUT)

    except Exception as ex:
        exception_response(ex)
        return "exception occured", 400

