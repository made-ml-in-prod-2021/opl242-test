import click
import logging
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


logger = logging.getLogger(__name__)

DATA_FILE = 'data.csv'
TARGET_FILE = 'target.csv'


@click.command()
@click.option("--data_dir")
@click.option("--output_dir")
@click.option("--ratio", type=float)
def split(data_dir: str, output_dir: str, ratio: float = 0.5):

    logger.info("Start splitting data")

    if data_dir is None:
        path_to_data = Path() / DATA_FILE
        path_to_target = Path() / TARGET_FILE
    else:
        path_to_data = Path(data_dir) / DATA_FILE
        path_to_target = Path(data_dir) / TARGET_FILE

    if not path_to_data.is_file():
        logger.error(f"Data file not found")
        return

    data = pd.read_csv(path_to_data, header=None)
    target = pd.read_csv(path_to_target, header=None)

    X_train, X_test, y_train, y_test = train_test_split(
        data, target, train_size=ratio
    )

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    X_train.to_csv(
        output_dir / 'X_train.csv', header=False, index=False,
    )

    y_train.to_csv(
        output_dir / 'y_train.csv', header=False, index=False,
    )

    X_test.to_csv(
        output_dir / 'X_test.csv', header=False, index=False,
    )

    y_test.to_csv(
        output_dir / 'y_test.csv', header=False, index=False,
    )

    logger.info("End of splitting data")


if __name__ == '__main__':
    split()