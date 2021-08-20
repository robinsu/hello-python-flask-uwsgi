import logging
logger = logging.getLogger(__name__)

import json
from flask import Blueprint, jsonify, request
from flaskr.db import get_db_engine
from sqlalchemy import text
import time;
from datetime import datetime, timedelta, timezone

retail = Blueprint(name="/api/retail", import_name=__name__)

@retail.route('/checkin', methods=['GET', 'POST'])
def checkin():
    """
    """
    output={ 'status': "0" }
    logging.info(f"checkin( {request.get_json()} )")
    try:
        qrcode = request.get_json().get('qrcode')
        trigger_time = request.get_json().get('trigger_time')
        store_id = request.get_json().get('store_id')
        status = request.get_json().get('status')
        status_msg = request.get_json().get('status_msg')
        
        output['status'] = "1"
        output['status_msg'] = "welcome"
        output['uid'] = qrcode
        output['uid_type'] = "cus"
    except Exception as err:
        logging.error('Unexpected error at %s', err, exc_info=err)
        output['msg'] = f"Unexpected error: {str(err)}"
    return jsonify(output)


@retail.route('/test', methods=['GET'])
def test():
    """
    ---
    get:
      description: test endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing
    """
    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)