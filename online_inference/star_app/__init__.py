from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import pandas as pd


from .config import Config
from .models.load_model import load_model


def setup_logging(app):
    file_handler = RotatingFileHandler(app.config['LOGFILE'], 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('online_inference startup')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    setup_logging(app)    

    from star_app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    app.model = load_model(app.config['MODEL_PATH'])
    df = pd.read_csv(app.config['COLOR_CODES_PATH'])
    app.color_codes = {val: code for code, val in df.values}
    df = pd.read_csv(app.config['CLASS_CODES_PATH'])
    app.class_codes = {code: val for code, val in df.values}

    return app