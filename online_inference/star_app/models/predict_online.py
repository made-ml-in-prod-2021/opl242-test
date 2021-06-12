import numpy as np
from flask import current_app


from ..entities.config import modelFieldsSchema


def predict_online(data: modelFieldsSchema):
    x_row = []
    for field in current_app.config['FIELDS']:
        if field != 'color':
            x_row.append(data.__dict__.get(field))
        else:
            x_row.append(
                current_app.color_codes.get(
                    data.color, current_app.config['DEFAULT_COLOR_CODE']
                )
            )
    
    X = np.array(x_row).reshape(1, -1)
    class_code = current_app.model.predict(X)
    return current_app.class_codes.get(
        class_code[0], current_app.config['UNKNOWN_CLASS']
    )