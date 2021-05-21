import pytest
from pathlib import Path
from sklearn.dummy import DummyClassifier

from ml_project.models.save_model import save_model


# -----------------------------------------------------------------------------
def test_save_model_1(hydra_cfg, tmpdir, dummy_model):
    hydra_cfg.model.store_path = str(Path(tmpdir / 'model.pkl'))
    save_model(hydra_cfg.model, dummy_model)
    assert Path(hydra_cfg.model.store_path).is_file()
