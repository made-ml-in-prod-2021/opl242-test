import click
import logging
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

MODEL_FILE = 'model.pkl'
VALIDATION_FILE = 'validation.txt'

logger = logging.getLogger(__name__)

@click.command()
@click.option("--data_dir")
@click.option("--model_dir")
@click.option("--val_dir")
def train(data_dir: str, model_dir: str, val_dir: str):
    logger.info("Start model evaluation")
    test_X = pd.read_csv(Path(data_dir) / 'X_test.csv', header=None)
    test_y = pd.read_csv(Path(data_dir) / 'y_test.csv', header=None)

    with open(Path(model_dir) / MODEL_FILE, "rb") as fin:
        model = pickle.load(fin)
    logger.info("Model is loaded")

    y_pred = model.predict(test_X)
    logger.info("Test data predicted")

    val = f1_score(y_pred, test_y, average='micro')

    val_dir = Path(val_dir)
    val_dir.mkdir(exist_ok=True, parents=True)
    with open(val_dir / VALIDATION_FILE, 'wt') as fout:
        fout.write(str(val))
    logger.info("Model is saved")


if __name__ == '__main__':
    train()