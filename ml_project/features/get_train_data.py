import pandas as pd
from sklearn.model_selection import train_test_split
from omegaconf import DictConfig


# -----------------------------------------------------------------------------
def get_train_data(
    model_cfg: DictConfig,
    df: pd.DataFrame,
    test_size: float = None
) -> tuple:

    test_size = test_size or model_cfg.test_size
    X = df.drop(model_cfg.target_col, axis=1)
    y = df[model_cfg.target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=model_cfg.random_state
    )
    return X_train, X_test, y_train, y_test
