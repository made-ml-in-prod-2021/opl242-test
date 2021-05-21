import pandas as pd
from sklearn.base import ClassifierMixin


# -----------------------------------------------------------------------------
def predict_model(model: ClassifierMixin, X: pd.DataFrame) -> int:
    y = model.predict(X)
    return y