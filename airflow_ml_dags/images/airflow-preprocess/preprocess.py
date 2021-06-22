import pandas as pd
import click
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


@click.command()
@click.option("--input_dir")
@click.option("--output_dir")
def preprocess(input_dir: str, output_dir:str):
    logger.info("Start data preprocessing")
    data = pd.read_csv(Path(input_dir) / "data.csv", header=None)
    target = pd.read_csv(Path(input_dir) / "target.csv", header=None)

    class_codes = pd.read_csv("class_codes.csv", header=None)

    target = target.merge(class_codes, left_on=0, right_on=1, how='left')
    print(target)

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    data.to_csv(
        output_dir / 'data.csv', mode='a', header=False, index=False,
    )

    target["0_y"].to_csv(
        output_dir / 'target.csv', mode='a', header=False, index=False,
    )
    logger.info("End of data preprocessing")


if __name__ == '__main__':
    preprocess()