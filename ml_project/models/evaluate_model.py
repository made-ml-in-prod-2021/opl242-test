import logging
import pandas as pd
from sklearn.metrics import f1_score


logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
def evaluate_model(
    y_pred: pd.Series,
    y_true: pd.Series,
) -> float:

    score = f1_score(y_pred, y_true, average="micro")
    logger.info(f"score is {score}")
    return score