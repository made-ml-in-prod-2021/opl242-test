# opl242-test

# Project for MADE 2021 #

MADE profile link:
https://data.mail.ru/profile/a.opolchenov/

## Installation:##

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt


## Usage: ##

    Usage: make_prediction.py [OPTIONS]

    Options:
    --ip TEXT              Server IP
    --port INTEGER         Server port
    --temperature INTEGER  Temperature (K)
    --luminocity FLOAT     Luminosity(L/Lo)
    --radius FLOAT         Radius(R/Ro)
    --magnitude FLOAT      Absolute magnitude(Mv)
    --type INTEGER         Star type
    --color TEXT           Star color
    --help                 Show this message and exit.
    
Usage example:

    python make_prediction.py --temperature=3068 --luminocity=0.17 --radius=16.12 --
type=0 --color="red"
    "M"

## Tets: ##

    pytest -v tests\
