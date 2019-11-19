from app.verification.verification_core import get_structures, ocr_core
from utils.text_utils import *
import base64
import cv2
import numpy as np
import logging
logger = logging.getLogger(__name__)


def info_extraction_service(response_object):
    string = response_object['image']
    jpg_original = base64.b64decode(string)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    sample_response = ocr_core(img)
    response_data = create_response_object(len(sample_response), sample_response, STATUS_SUCCESS)
    return response_data


def logo_extraction_service(response_object):
    string = response_object['image']
    jpg_original = base64.b64decode(string)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    sample_response = get_structures(img)
    response_data = create_response_object(len(sample_response), sample_response, STATUS_SUCCESS)
    return response_data


def create_response_object(len_data, data, message):
    """ Function to """
    if len_data != 0:
        response = {'status': "OK", 'message': message,
                    'result': data}
        logger.info(message)
        return response
    else:
        response = {'status': "Failed", 'message': message,
                    'result': data}
        return response
