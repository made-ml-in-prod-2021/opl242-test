from flask import current_app, jsonify, request
from marshmallow.exceptions import ValidationError


from . import bp
from .errors import bad_request
from ..entities.config import modelFieldsSchema
from ..models.predict_online import predict_online


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
    
    