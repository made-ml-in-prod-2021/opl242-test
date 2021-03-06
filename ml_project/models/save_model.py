import logging
import pickle
from pathlib import Path
from omegaconf import DictConfig
from sklearn.base import ClassifierMixin


logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
def save_model(model_cfg: DictConfig, model: ClassifierMixin) -> bool:
    with open(Path(__file__).parent.parent / model_cfg.store_path, 'wb') as fout:
        pickle.dump(model, fout)
    logger.info("Model is saved")