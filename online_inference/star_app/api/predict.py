from flask import current_app, jsonify, request
from marshmallow.exceptions import ValidationError
import os
import time

from . import bp
from .errors import bad_request
from ..entities.config import modelFieldsSchema
from ..models.predict_online import predict_online
from flask import current_app

TIME_TO_CRASH = 60


@bp.route('/health', methods=['GET'])
def check_health():
    global app
    if time.time() - current_app.start_time > TIME_TO_CRASH:
        current_app.logger.critical("Too much for me, I need some rest, sorry...")
        os._exit(242)
    if current_app.model is not None:
        return jsonify({'success':True})
    else:
        return bad_request("service is not ready")


@bp.route('/predict', methods=['GET'])
def predict():
    data = request.get_json() or {}
    no_fields = []
    record = {}
    for field in current_app.config['FIELDS']:
        if field not in data:
            no_fields.append(field)
        else:
            record[field] = data[field]
    if len(no_fields) > 0:
        current_app.logger.error(f"{', '.join(no_fields)} must be in request data")
        return bad_request(f"{', '.join(no_fields)} must be in request data")

    try:
        record_row = modelFieldsSchema.load(data=record)
    except ValidationError as e:
        current_app.logger.error(f"{e}")
        return bad_request(f"{e}")
    result = predict_online(record_row)
    current_app.logger.info(f"prediction for {record} is {result}")
    return jsonify(result)
    
    