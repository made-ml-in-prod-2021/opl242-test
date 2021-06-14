import hydra
import numpy as np
import pandas as pd
import logging
from omegaconf import DictConfig
from pathlib import Path


logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
@hydra.main(config_path="", config_name="config.yaml")
def generate_test_data(
    hydra_cfg: DictConfig, 
):
    """ generating fake data for tests

    Args:
        n_rows (int, optional): number of rows. Defaults to 10.

    Returns:
        DataFrame: random data
    """
    logger.info("data generation started")
    row = {}
    for par in hydra_cfg.data_generation:
        if hydra_cfg.data_generation[par].is_int:
            fun = np.random.randint
        else:
            fun = np.random.uniform      
        row[par] = fun(
            hydra_cfg.data_generation[par].min,
            hydra_cfg.data_generation[par].max,
            hydra_cfg.n_rows
        )
    df = pd.DataFrame(row)
    output_dir = Path(hydra_cfg.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    # df.drop('type')
    df.to_csv(
        output_dir / 'data.csv', mode='a', header=False, index=False,
    )

    trg_lst = [np.random.choice(list(hydra_cfg.target)) for q in range(hydra_cfg.n_rows)]
    trg_df = pd.DataFrame(trg_lst)
    trg_df.to_csv(
        output_dir / 'target.csv', mode='a', header=False, index=False,
    )
    # print([q for q in Path(output_dir).glob("*")])
    logger.info("data generation finished")


if __name__ == "__main__":
    print(Path().absolute())
    generate_test_data()