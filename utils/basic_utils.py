from flask import jsonify
from utils.text_utils import *

import logging
logger = logging.getLogger(__name__)


# show response when exception occur
def exception_response(ex):
    message = ERROR_EXCEPTION_OCCUR.format(type(ex).__name__, ex.args)
    logger.error(message, exc_info=True)
    response = error_response(message)
    return jsonify(response)


# show response for errors
def error_response(msg, result=None):
    logger.error(msg)
    response = {'status': STATUS_FAILED, 'message': msg, 'result': result}
    return jsonify(response)
