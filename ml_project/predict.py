from ml_project.data.make_dataset import make_dataset
import click
import hydra
from pathlib import Path
import pandas as pd
import pickle
from omegaconf import DictConfig

from .data.make_dataset import make_dataset


# -----------------------------------------------------------------------------
def predict(model_path: Path, path_to_x: Path):
    with open(Path(__file__).parent.parent / model_path, "rb") as fin:
        model = pickle.load(fin)
    X = make_dataset(Path(__file__).parent.parent / path_to_x)
    y = model.predict(X)
    return y


# -----------------------------------------------------------------------------
@click.command()
@click.option(
    '--model_path', type=click.Path(exists=True),
    default="models/model.pkl",
    help="Path to stored trained model"
)
@click.option(
    '--path_to_x', type=click.Path(exists=True),
    default="data/raw/data_to_predict.csv",
    help="Path to raw data for predictions"
)
def main(model_path: Path, path_to_x: Path):
    y = predict(model_path, path_to_x)
    print(y)    

if __name__ == "__main__":
    main()
