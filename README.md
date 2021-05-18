# opl242-test

# Project for MADE 2021 #

MADE profile link:
https://data.mail.ru/profile/a.opolchenov/

## Installation:##

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt


## Usage: ##

Train model:

    python -m ml_project.train_pipeline

Config file config/config.yaml

You could change config params in cli:

    python -m ml_project.train_pipeline data.raw="../data/raw/stars_2.csv" model.max_depth=3

Model inferece:

    python -m ml_project.predict.py [OPTIONS]

    Options:
    --model_path PATH  Path to stored trained model
    --path_to_x PATH   Path to raw data for predictions
    --help             Show this message and exit.


## Tets: ##

    pytest -v tests\