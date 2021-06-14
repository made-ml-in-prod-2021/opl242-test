import click
import logging
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

MODEL_FILE = 'model.pkl'

logger = logging.getLogger(__name__)

@click.command()
@click.option("--data_dir")
@click.option("--model_dir")
def train(data_dir: str, model_dir: str):
    logger.info("Start training model")
    train_X = pd.read_csv(Path(data_dir) / 'X_train.csv', header=None)
    train_y = pd.read_csv(Path(data_dir) / 'y_train.csv', header=None)

    model = RandomForestClassifier()
    model.fit(train_X, train_y)
    logger.info("Model is trained")

    model_dir = Path(model_dir)
    model_dir.mkdir(exist_ok=True, parents=True)
    with open(model_dir / MODEL_FILE, 'wb') as fout:
        pickle.dump(model, fout)
    logger.info("Model is saved")


if __name__ == '__main__':
    train()