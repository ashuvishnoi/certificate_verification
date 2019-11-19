import os
from flask_cors import CORS
from flask import Flask, jsonify
from flask_swagger import swagger
from utils.text_utils import *
from datetime import datetime, timedelta
from app.verification.verfication_controller import info_extraction_api
from app.verification.verfication_controller import logo_extraction_api

import logging
logging.basicConfig(level=logging.DEBUG)

# SETUP LOGGING
if not os.path.exists('logs'):
    os.makedirs('logs')

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
debug_handler = logging.FileHandler('logs/debug.log')
info_handler = logging.FileHandler('logs/info.log')
debug_handler.setLevel(logging.DEBUG)
info_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
converter = lambda x, y: (datetime.utcnow() + timedelta(hours=5, minutes=30)).timetuple()
logging.Formatter.converter = converter

debug_format = logging.Formatter('[%(asctime)s] {%(filename)s: %(lineno)d} %(levelname)s - %(message)s')
info_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(debug_format)
info_handler.setFormatter(info_format)

# Add handlers to the logger
logger.addHandler(debug_handler)
logger.addHandler(info_handler)


# SETUP FLASK SERVER
blueprint1 = info_extraction_api
blueprint2 = logo_extraction_api


# add Cross-Origin-Resource-Sharing support
CORS(blueprint1)
CORS(blueprint2)

#  Start the flask server
server = Flask(__name__)
server.register_blueprint(blueprint1)
server.register_blueprint(blueprint2)


@server.route("/", methods=['POST', 'GET'])
def spec():
    return jsonify(swagger(server))


