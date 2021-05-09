# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

from ml_project.features.build_features import process_raw_dataset


# -----------------------------------------------------------------------------
@click.command()
@click.argument(
    'input_filepath', type=click.Path(exists=True),
    default="../data/raw/stars.csv"
)
@click.argument(
    'output_filepath', type=click.Path(),
    default="../data/processed/stars.csv"
)
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    df = make_dataset(input_filepath, output_filepath)
    logger.info('dataset is ready')
    return df


# -----------------------------------------------------------------------------
def make_dataset(input_filepath, output_filepath) -> pd.DataFrame:
    df = pd.read_csv(input_filepath)
    df = process_raw_dataset(df)
    df.to_csv(output_filepath, index=False)
    return df


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
