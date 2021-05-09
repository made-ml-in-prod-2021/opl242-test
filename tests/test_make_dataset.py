import pytest
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pathlib import Path

from ml_project.data.make_dataset import make_dataset
from ml_project.entities.config import DataPathesSchema


def test_make_dataset_1(hydra_cfg, tmpdir):
    tmp_out = Path(tmpdir)/'out.csv'
    make_dataset(input_filepath=hydra_cfg.data.raw, output_filepath=tmp_out)
    df = pd.read_csv(tmp_out)
    assert df.shape == (240, 7), f'df.shape is {df.shape}'
    assert 'magnitude' in df.columns
    assert is_numeric_dtype(df.color)
