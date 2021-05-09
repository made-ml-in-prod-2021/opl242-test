import logging
from pathlib import Path
from omegaconf import DictConfig

from ml_project.data.make_dataset import make_dataset
from ml_project.features.get_train_data import get_train_data
from ml_project.models.build_model import build_model
from ml_project.models.train_model import train_model
from ml_project.models.predict_model import predict_model
from ml_project.models.evaluate_model import evaluate_model
from ml_project.models.save_model import save_model
from ml_project.train_pipeline import train_pipeline


logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
def test_train_e2e(hydra_cfg: DictConfig):
    logger.info("Pipeline starting...")
    
    data = make_dataset(hydra_cfg.data.raw, hydra_cfg.data.processed)
    X_train, X_test, y_train, y_test = get_train_data(hydra_cfg.model, data)
    logger.info("Data is ready...")
    model = build_model(hydra_cfg.model)
    logger.info("Model is ready...")
    model = train_model(model, X_train, y_train)
    logger.info("Model is trained...")
    y_pred = predict_model(model, X_test)
    score = evaluate_model(y_pred, y_test)
    save_model(hydra_cfg.model, model)
    logger.info("Model is saved...")
    logger.info(f"Model score is {score}")

    assert 0 <= score <= 1

