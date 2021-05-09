import logging
import pandas as pd
# from sklearn.base import ClassifierMixin
from sklearn.metrics import f1_score

# from ml_project.models.predict_model import predict_model


logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
def evaluate_model(
    # model: ClassifierMixin,
    # X_test: pd.DataFrame,
    y_pred: pd.Series,
    y_true: pd.Series,
) -> float:

    # y_pred = predict_model(model, X_test)
    score = f1_score(y_pred, y_true, average="micro")
    logger.info(f"score is {score}")
    return score