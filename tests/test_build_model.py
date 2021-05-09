import pytest
from sklearn.base import is_classifier
from omegaconf import DictConfig

from ml_project.models.build_model import build_model


# -----------------------------------------------------------------------------
def test_build_model_1(hydra_cfg: DictConfig):
    model = build_model(hydra_cfg.model)
    assert is_classifier(model)
