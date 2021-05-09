import logging
from sklearn.ensemble import RandomForestClassifier
from omegaconf import DictConfig
from sklearn.base import ClassifierMixin


logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
def build_model(model_cfg: DictConfig) -> ClassifierMixin:
    model = RandomForestClassifier(
        n_estimators=model_cfg.n_estimators,
        criterion=model_cfg.criterion,
        max_depth=model_cfg.max_depth,
    )
    logger.info('Model isInstance:')
    logger.info(isinstance(model, ClassifierMixin))
    return model