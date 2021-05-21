import pytest
import logging
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.base import is_classifier
from sklearn.base import ClassifierMixin


from ml_project.models.train_model import train_model
from ml_project.models.build_model import build_model
from ml_project.features.get_train_data import get_train_data


logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
def test_train_model_1(hydra_cfg, tmpdir, random_data):
    hydra_cfg.model.store_path = str(Path(tmpdir) / 'out.pkl')
    X_train, _, y_train, _ = get_train_data(
        model_cfg=hydra_cfg.model, df=random_data, test_size=0
    )
    model = build_model(hydra_cfg.model)
    logger.warning('Model isInstance:')
    logger.info(isinstance(model, ClassifierMixin))    
    train_model(model, X_train, y_train)
    assert is_classifier(model)
