import pickle
from sklearn.base import ClassifierMixin


def load_model(path_to_model: str) -> ClassifierMixin:
    with open(path_to_model, "rb") as fin:
        model = pickle.load(fin)
    return model
