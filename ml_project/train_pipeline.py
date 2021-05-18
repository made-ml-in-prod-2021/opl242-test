import hydra
import logging
import sys
from omegaconf import DictConfig

from .data.make_dataset import make_dataset
from .features.get_train_data import get_train_data
from .models.build_model import build_model
from .models.train_model import train_model
from .models.predict_model import predict_model
from .models.evaluate_model import evaluate_model
from .models.save_model import save_model


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# -----------------------------------------------------------------------------
def train_pipeline(hydra_cfg: DictConfig):
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


@hydra.main(config_path="../configs", config_name="config.yaml")
def main(cfg):
    train_pipeline(cfg)

if __name__ == "__main__":
    main()