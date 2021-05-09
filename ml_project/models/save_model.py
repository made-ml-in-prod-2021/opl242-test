import logging
import pickle
from omegaconf import DictConfig
from sklearn.base import ClassifierMixin


logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
def save_model(model_cfg: DictConfig, model: ClassifierMixin) -> bool:
    with open(model_cfg.store_path, 'wb') as fout:
        pickle.dump(model, fout)
    logger.info("Model is saved")