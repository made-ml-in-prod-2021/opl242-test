import click
import logging
import pickle
import numpy as np
import pandas as pd
from pathlib import Path

MODEL_FILE = "model.pkl"
DATA_FILE = "data.csv"
PREDICTION_FILE = 'prediction.csv'

logger = logging.getLogger(__name__)


@click.command()
@click.option("--input_dir")
@click.option("--model_dir")
@click.option("--output_dir")
def predict(input_dir: str, model_dir: str, output_dir: str):
    logger.info("Start prediction")

    data = pd.read_csv(Path(input_dir) / DATA_FILE, header=None)

    with open(Path(model_dir) / MODEL_FILE, "rb") as f:
        model = pickle.load(f)
    
    prediction = model.predict(data).astype(np.int)

    Path(output_dir).mkdir(exist_ok=True, parents=True)

    np.savetxt(Path(output_dir) / PREDICTION_FILE, prediction)
    logger.info("Prediction saved")


if __name__ == "__main__":
    predict()