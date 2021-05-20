import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secret-key'
    FIELDS = ['temperature', 'luminocity', 'radius', 'magnitude', 'type', 'color']
    MODEL_PATH = "../models/model.pkl"
    COLOR_CODES_PATH = "../models/color_codes.csv"
    CLASS_CODES_PATH = "../models/class_codes.csv"
    LOGFILE = "online_inference.log"
    UNKNOWN_CLASS = "Unknown"
    DEFAULT_COLOR_CODE = 3