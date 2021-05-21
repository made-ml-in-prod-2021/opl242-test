import pandas as pd
from sklearn.base import ClassifierMixin

# -----------------------------------------------------------------------------
def train_model(
    model: ClassifierMixin, X_train: pd.DataFrame, y_train: pd.Series
):
    model.fit(X_train, y_train)
    return model