import pytest
import logging
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from omegaconf import DictConfig
from hydra.experimental import compose, initialize


from ml_project.features.get_train_data import get_train_data


HYDRA_CONFIG_PATH = "../configs"
HYDRA_CONFIG_FILENAME = "config.yaml"

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger()


# -----------------------------------------------------------------------------
def generate_test_data(hydra_cfg: DictConfig, n_rows: int = 10):
    """ generating fake data for tests

    Args:
        n_rows (int, optional): number of rows. Defaults to 10.

    Returns:
        DataFrame: random data
    """
    row = {}
    for par in hydra_cfg.data_generation:
        if hydra_cfg.data_generation[par].is_int:
            fun = np.random.randint
        else:
            fun = np.random.uniform      
        row[par] = fun(
            hydra_cfg.data_generation[par].min,
            hydra_cfg.data_generation[par].max,
            n_rows
        )
    return pd.DataFrame(row)


# -----------------------------------------------------------------------------
@pytest.fixture(scope='session')
def hydra_cfg() -> DictConfig:
    """ load configuration

    Returns:
        DictConfig: configuration
    """
    initialize(config_path=HYDRA_CONFIG_PATH)
    conf = compose(HYDRA_CONFIG_FILENAME)
    return conf


# -----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def dummy_model() -> DummyClassifier:
    """ dummy model for testing operations with models

    Returns:
        DummyClassifier: model
    """
    model = DummyClassifier()
    return model


# -----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def dummy_trained_model(hydra_cfg: DictConfig, dummy_model, random_data) -> DummyClassifier:
    """ dummy model trained on random data

    Returns:
        DummyClassifier: trained model
    """
    X_train, _, y_train, _ = get_train_data(
        model_cfg=hydra_cfg.model, df=random_data, test_size=0
    )

    dummy_model.fit(X_train, y_train)
    return dummy_model


# -----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def random_data(hydra_cfg: DictConfig) -> pd.DataFrame:
    """ generate ramdom data

    Args:
        hydra_cfg (DictConfig): configuration of data

    Returns:
        pd.DataFrame: generated data
    """
    return generate_test_data(hydra_cfg)


# -----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def random_data_x(
    hydra_cfg: DictConfig,
    random_data: pd.DataFrame
) -> pd.DataFrame:
    """ generate ramdom data, X only

    Args:
        hydra_cfg (DictConfig): configuration of data

    Returns:
        pd.DataFrame: generated data
    """
    X_train, _, _, _ = get_train_data(
        model_cfg=hydra_cfg.model, df=random_data, test_size=0
    )
    return X_train


# -----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def random_data_y(
    hydra_cfg: DictConfig,
    random_data: pd.DataFrame
) -> pd.DataFrame:
    """ generate ramdom data, y only

    Args:
        hydra_cfg (DictConfig): configuration of data

    Returns:
        pd.DataFrame: generated data
    """
    return random_data[hydra_cfg.model.target_col]
    # _, _, y_train, _ = get_train_data(
    #     model_cfg=hydra_cfg.model, df=random_data, test_size=0
    # )
    # return y_train
