# -*- coding: utf-8 -*-
import os
from flask import jsonify
import logging
import time
from flask_app import app, api_bp
from .utils import *

logger = logging.getLogger(__name__)

print("load function.")
        
@api_bp.route('/hello', methods=['GET'])
def hello():
    try:
        dic_status = { "hello": "world" }
        return jsonify(dic_status)
    except Exception as err:
        logger.error("Fatal error in %s", err, exc_info=True)
        status = {"Fatal": str(err)}
        return jsonify(status)

